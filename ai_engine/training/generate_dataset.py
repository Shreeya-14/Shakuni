"""Dataset Generator and Curator for Shakuni.

Constructs the comprehensive research dataset across all 7 manipulation categories:
1. Normal / No Significant Manipulation
2. Social Pressure
3. Emotional Pressure
4. Misleading Framing
5. Selective Information
6. Information Withholding
7. Deceptive Persuasion

Preserves original research samples, incorporates diverse everyday conversational utterances,
meeting notices, non-coercive emotional expressions, rational arguments, hard negatives,
and contrastive pairs.

Splits data into stratified train (70%), validation (15%), and test (15%) sets without leakage.
"""

import os
import csv
import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# All 7 canonical categories
NORMAL_CAT = "Normal / No Significant Manipulation"
SOCIAL_CAT = "Social Pressure"
EMOTIONAL_CAT = "Emotional Pressure"
FRAMING_CAT = "Misleading Framing"
SELECTIVE_CAT = "Selective Information"
WITHHOLDING_CAT = "Information Withholding"
DECEPTIVE_CAT = "Deceptive Persuasion"

# Comprehensive Curated Dataset
EXPANDED_CATEGORIES_DATA = {
    NORMAL_CAT: [
        # --- Original formal corporate & technical announcements (40) ---
        "The scheduled software release has been postponed to Tuesday to complete standard regression testing.",
        "Our quarterly financial review will take place in Conference Room B at 2:00 PM tomorrow.",
        "Please review the attached pull request and verify that unit tests pass in your local environment.",
        "The laboratory confirmed that the water sample adheres to municipal drinking safety guidelines.",
        "We have published the updated user manual on the internal documentation portal for your reference.",
        "The train departure from platform 4 is delayed by approximately fifteen minutes due to track maintenance.",
        "Our survey results indicate that sixty-four percent of participants prefer flexible remote work hours.",
        "All employee travel expenses must be submitted with accompanying itemized receipts by month end.",
        "The data migration script will run overnight to avoid interference with normal operational hours.",
        "The meeting minutes from yesterday's architectural sync have been uploaded to the project wiki.",
        "The conference keynote starts at 9:00 AM, followed by technical breakout sessions in the afternoon.",
        "System maintenance is scheduled for Sunday between 1:00 AM and 3:00 AM UTC.",
        "We observed a three percent increase in page load time after deploying the new caching layer.",
        "The study analyzed demographic trends across six metropolitan regions over a ten-year duration.",
        "The annual security audit will begin next Monday and will include vulnerability scanning.",
        "Please confirm your attendance for the upcoming stakeholder presentation before Thursday noon.",
        "The shipment of replacement hardware components arrived at the distribution warehouse this morning.",
        "Both candidate algorithms achieved comparable latency profiles across synthetic benchmark workloads.",
        "The university library will remain open twenty-four hours during the upcoming final examination week.",
        "The revised departmental budget allocations will take effect at the start of the next fiscal quarter.",
        "Our customer support team is available Monday through Friday from 8:00 AM to 6:00 PM EST.",
        "The compiler outputs a warning when unused variables are detected in the global namespace.",
        "The research team compiled twenty peer-reviewed studies examining climate adaptation strategies.",
        "Feedback on the draft syllabus should be emailed to the curriculum committee by the end of next week.",
        "The building management announced routine fire alarm inspections for tomorrow morning between 10 and 11 AM.",
        "The latest firmware release includes bug fixes for Bluetooth pairing instability on older devices.",
        "Project deliverables must be archived in the central repository within two weeks of milestone completion.",
        "The cafeteria will offer vegetarian and gluten-free lunch options starting next Monday.",
        "A formal summary of today's customer advisory council will be distributed to product leads tomorrow.",
        "The sensor measures ambient temperature and humidity at thirty-second intervals continuously.",
        "Please verify your contact details in the human resources directory before the end of the month.",
        "The evaluation committee evaluated forty-five grant proposals using a standardized scoring rubric.",
        "Network latency between the Frankfurt and London datacenters averaged twenty-one milliseconds.",
        "The research team documented baseline experimental parameters prior to initiating the second phase.",
        "New employees are required to complete the mandatory orientation module within thirty days of joining.",
        "The solar panel array generated forty-eight kilowatt-hours of electrical energy during peak sunlight.",
        "The committee approved the standard vendor contract terms with no amendments requested.",
        "The revised academic calendar incorporates three scheduled reading days prior to final examinations.",
        "The team concluded sprint planning and assigned tasks across the upcoming two-week development cycle.",
        "Please ensure all laboratory equipment is powered down and secured before exiting the facility.",

        # --- Meeting schedules, attendance reminders, deadlines (Everyday & Conversational) ---
        "There is a meeting tomorrow.",
        "The meeting is scheduled for tomorrow.",
        "Please attend the meeting at 10 AM.",
        "The report must be submitted by Friday.",
        "The weekly sync will take place on Wednesday morning.",
        "Don't forget that our team retrospective is tomorrow at 3 PM.",
        "Our project kickoff call is set for next Monday at 11:00 AM.",
        "Please remember to submit your weekly timesheet before leaving today.",
        "The client presentation is tomorrow afternoon in Conference Room 3.",
        "The deadline for submitting conference abstracts is midnight tonight.",
        "Please join the standup call five minutes early if you have video setup questions.",
        "Our sprint demo will be held on Friday at 4 PM in the main auditorium.",
        "Let's move our one-on-one meeting to Thursday because of the conflicting workshop.",
        "The finance committee will convene tomorrow morning to review the quarterly numbers.",
        "The final draft of the research paper must be sent to the publisher by next Friday.",

        # --- Ordinary questions, requests, and polite workplace communication ---
        "Could you send me the latest slide deck when you get a chance?",
        "Can you please review line 42 of the pull request when you have time?",
        "Where can I find the documentation for the authentication service?",
        "Would you mind sharing the spreadsheet from yesterday's presentation?",
        "Could we schedule twenty minutes next week to talk through the database schema?",
        "Please let me know if you need any additional logs or stack traces to debug the issue.",
        "Can someone point me to the onboarding guide for the backend repository?",
        "Thank you for reviewing the pull request, I have addressed all of your comments.",
        "Please let me know your availability for a brief sync later this afternoon.",
        "Could you please confirm whether the staging deployment finished successfully?",

        # --- Hard negatives: Sentences containing 'everyone', 'all', 'decision', 'urgency', 'CEO' ---
        "Everyone received the announcement yesterday.",
        "Everyone in our engineering division attended the mandatory security briefing.",
        "All team members were added to the updated calendar invite.",
        "All engineers submitted their annual self-evaluations before the deadline.",
        "We need to make a decision today.",
        "We need to make a decision today because the vendor's discount offer expires at 5 PM.",
        "The team needs to decide between PostgreSQL and MySQL for the new analytics database.",
        "The CEO sent an organization-wide email thanking employees for their contributions.",
        "The CEO announced the company's annual financial results during this morning's town hall.",
        "Everyone on the distribution list was notified of the network downtime.",
        "All participants must register at the reception desk before entering the conference hall.",
        "We must patch this critical security vulnerability immediately to protect customer data.",
        "The server CPU usage spiked to ninety-nine percent, so we need to restart the worker node immediately.",

        # --- Subjective emotion & personal feelings without coercion ---
        "I am worried about the deadline.",
        "I feel really stressed about the client presentation tomorrow.",
        "I am anxious about whether our proposal will be accepted by the grant committee.",
        "I am disappointed that the release date had to be pushed back again.",
        "I feel overwhelmed with the number of incoming support tickets today.",
        "I am excited to see the positive customer feedback from this morning's release.",
        "I am nervous about leading the company-wide all-hands meeting next week.",
        "I am frustrated with this intermittent networking bug, but I will keep investigating.",
        "I am concerned that our current server infrastructure might not handle Black Friday traffic.",
        "I feel relieved that all integration tests passed on the continuous integration server.",

        # --- Disagreements and opinions without coercion ---
        "I disagree with your proposal, but I understand the trade-offs you considered.",
        "In my opinion, we should wait for more user research data before changing the navigation.",
        "I have a different perspective on this architecture and would prefer to use gRPC over REST.",
        "I respectfully disagree with the conclusion reached in this benchmark report.",
        "While I understand your point, I think maintaining backwards compatibility is more important here.",
        "I suggest we look into alternative caching strategies before investing in additional servers.",
        "From an engineering standpoint, I believe refactoring the billing module now will save time later.",

        # --- Legitimate persuasion & rational justification (Contrastive to Deception) ---
        "I strongly recommend this option because it reduces costs.",
        "I strongly recommend migrating to containerized deployments because it standardizes our environments.",
        "We should adopt automated testing because it catches regressions before they reach production.",
        "This architectural pattern is preferable because it decouples our frontend from database migrations.",
        "I advise using Redis for session management because it significantly reduces database query load.",
        "We should hire a dedicated UX designer because user drop-off rates on our checkout page are high.",
        "Investing in static code analysis will help our junior developers identify security vulnerabilities early.",

        # --- Balanced discussion of pros and cons (Contrastive to Misleading Framing) ---
        "This plan has benefits, but it also has drawbacks.",
        "The proposed microservices architecture offers greater modularity, though it introduces network latency.",
        "While the new database engine improves read throughput, write latency is slightly higher.",
        "There are valid arguments on both sides of whether to open-source this library.",
        "The redesign improves mobile accessibility, although desktop power users may need time to adapt.",
        "Both candidate frameworks have strong community support and comparable documentation.",
        "The vendor provides excellent uptime, but their licensing fees are significantly higher than open-source alternatives."
    ],

    SOCIAL_CAT: [
        # --- Original samples (40) ---
        "Everyone on the leadership team has already signed off on this initiative, so don't be the lone dissenter.",
        "All the other senior engineers agreed to work over the weekend; are you really going to let the team down?",
        "Nobody in our organization questions these operational procedures if they want to remain in good standing.",
        "Every modern tech enterprise has adopted this framework; choosing anything else will make us look amateurish.",
        "All your colleagues have already contributed to the departmental gift; your name is the only one missing.",
        "If you want to be viewed as a serious contender for promotion, you will publicly endorse the CEO's proposal.",
        "The entire team is counting on you to conform to our established protocol without raising objections.",
        "Everyone else completed the survey in support of management's restructuring; don't be difficult.",
        "Smart professionals never push back against executive consensus unless they have an alternative job lined up.",
        "Every single department head attended the voluntary workshop; your absence was noticed by senior partners.",
        "Our top performers don't complain about eighty-hour work weeks; they step up and prove their commitment.",
        "Everyone agrees that this compromise is the only sensible choice, so your resistance seems entirely unreasonable.",
        "If you speak out against this policy in the town hall, you will quickly alienate your most influential peers.",
        "Do you really want to be the sole developer remembered for blocking a high-profile corporate product launch?",
        "All the respected researchers in this field support this methodology; rejecting it will isolate your lab.",
        "Every reputable company in our industry complies with these guidelines without making excuses.",
        "The whole office has embraced the new culture shift, so why are you clinging to outdated traditions?",
        "Our highest-achieving team members always volunteer for late shifts without needing to be coaxed.",
        "Nobody likes a contrarian who disrupts team harmony right when we are about to present to investors.",
        "All of your peers have adopted the recommended workflow; continuing with your old setup looks insubordinate.",
        "Real team players do not ask tedious questions when the entire group has already committed to moving forward.",
        "Everyone else found the target realistic; claiming it is unachievable will reflect poorly on your capability.",
        "Look around you, everyone has agreed to the revised terms; why must you always create friction?",
        "The consensus across the entire advisory board is unanimous, and dissenting opinions will not be welcomed.",
        "All competitive firms are adopting this strategy; hesitation will make our board look completely clueless.",
        "Nobody wants to be the person who brought down team morale right before the funding round closes.",
        "All dedicated team members put company objectives ahead of personal commitments during crunch periods.",
        "Everyone else embraced the restructuring enthusiastically; your lack of excitement is quite noticeable.",
        "The entire senior cadre stands united behind this vision; breaking ranks will ruin your professional standing.",
        "You don't want your colleagues to think you aren't pulling your weight on this critical joint initiative.",
        "Every respectable practitioner endorses this protocol; divergence indicates a lack of professional rigor.",
        "Our division achieved record participation because nobody wanted to be left out of the recognition ceremony.",
        "Don't isolate yourself from the rest of the cohort by refusing to participate in the mandatory social outing.",
        "All the serious candidates for the fellowship have already published three papers; you are lagging behind.",
        "Your teammates are sacrificing their personal evenings; your refusal to do so demonstrates poor camaraderie.",
        "Nobody in this building disputes the executive director's authority on strategic realignment.",
        "Everyone in our peer group has upgraded to the premium subscription tier; don't get left behind.",
        "If you genuinely respect the collective judgment of the faculty, you will withdraw your public objection.",
        "The entire committee voted affirmatively; being the solitary dissenting voice will only damage your credibility.",
        "Top-tier contributors do not hesitate when the entire group steps up to meet an aggressive deadline.",

        # --- Additional diverse & contrastive samples (30) ---
        "Everyone agrees with me, so you should too.",
        "Literally everyone in this office supports the change; why are you the only one fighting it?",
        "All of your coworkers have already agreed to this pay cut; don't be the greedy one who ruins it for everyone.",
        "If you disagree with the group decision, you are simply showing that you don't belong in this culture.",
        "Nobody else on this floor has any complaints about management, so clearly the issue is with your attitude.",
        "Every respected engineer has moved past this technology; sticking with it makes you look totally incompetent.",
        "The rest of the squad has already put in extra hours; your refusal to match them shows zero team loyalty.",
        "Everyone in our circle has invested in this fund; do you really want to be the odd one out left behind?",
        "If you want to maintain your reputation in this firm, you will smile and nod during the partner's address.",
        "All reasonable people see that this policy is necessary; your hesitation makes you look obstinate.",
        "The whole department is aligned on this; dissenting now will permanently label you as difficult to work with.",
        "Nobody wants to work with a teammate who constantly questions what the group has already approved.",
        "Every other team hit their target without making excuses; why is your squad the only one complaining?",
        "If you vote against the majority on this motion, your peers will remember it when your promotion comes up.",
        "Everyone else accepted the revised role description without argument; why do you think you deserve special terms?",
        "Don't be the stubborn holdout who stops the entire organization from celebrating an on-time release.",
        "All top-tier professionals follow this consensus; deviating from it signals a lack of competence.",
        "The whole room nodded in agreement with the director; speaking out will only isolate you professionally.",
        "Everyone on Slack reacted with thumbs up; your silence is being noticed and interpreted as disapproval.",
        "Real professionals know when to swallow their pride and fall in line with the consensus.",
        "Nobody respects someone who breaks ranks when the entire battalion has committed to an assault.",
        "All your friends in the department have signed the petition; your refusal to sign will look like a betrayal.",
        "Everyone who matters in this company backs the initiative; pushing against it is career suicide.",
        "Your fellow interns are working through the weekend; taking Sunday off will make you look unmotivated.",
        "The whole community agrees this is the moral path; anyone opposing it is acting in bad faith.",
        "Every other department accepted the budget freeze quietly; making a fuss will make us look undisciplined.",
        "You don't want to be the reason why the entire team loses its quarterly performance bonus, do you?",
        "Everyone who understands modern business supports this merger; skepticism only reveals your inexperience.",
        "The consensus has already formed; continuing to raise objections just proves you aren't a collaborative player.",
        "All successful founders in our accelerator adopted this playbook; ignoring it guarantees your startup will fail."
    ],

    EMOTIONAL_CAT: [
        # --- Original samples (40) ---
        "If you really loved our family and cared about our happiness, you wouldn't accept that overseas job offer.",
        "I poured my heart, soul, and life savings into this business, and your hesitation is destroying my dreams.",
        "How could you betray my trust after everything I have sacrificed to help you succeed in this company?",
        "If you walk away from this project now, innocent people will suffer and the guilt will haunt you forever.",
        "I haven't slept in three weeks trying to protect your reputation, and this callous indifference is how you repay me?",
        "If you truly cared about our team's mission, giving up your personal weekend wouldn't even be a question.",
        "Think of the agonizing disappointment your parents will experience if you abandon this prestigious career path.",
        "I put my entire professional standing on the line to vouch for you, and your defiance is a slap in my face.",
        "You are breaking your mother's heart by refusing to attend the family gathering this Thanksgiving.",
        "If you report this minor discrepancy to auditors, you will ruin my life and put my children out on the street.",
        "How can you sit there so coldly while our entire organization teeters on the brink of catastrophic collapse?",
        "I am begging you on my knees to reconsider; you have the power to save me from total personal devastation.",
        "If you cared even a fraction as much as I do, you would feel deeply ashamed of your complete lack of effort.",
        "Your cold, calculated detachment proves that you never valued our friendship or our shared history.",
        "I sacrificed my own promotion last year so that you could advance, and now you abandon me at my lowest point.",
        "Every ounce of joy in my life has evaporated because of your relentless, unyielding stubbornness.",
        "If you have a shred of human empathy left in your soul, you will agree to withdraw your formal complaint.",
        "Think of how humiliated and broken you will feel when everyone discovers that you caused this catastrophe.",
        "I have given you everything a mentor could offer, and watching you turn against me is pure torture.",
        "If our startup fails because you refused to work late tonight, you will carry that moral burden forever.",
        "You are acting with such cruel selfishness that it makes me physically sick to look at you right now.",
        "I stayed up all night crying over your harsh email; I can't believe someone I loved could be so heartless.",
        "If you don't grant this extension, my career is completely finished and it will be entirely your doing.",
        "Please don't abandon me right now; without your financial help, I literally have nowhere else to turn.",
        "Your refusal to compromise is tearing this close-knit family apart and destroying decades of harmony.",
        "I took the blame for your mistake during the client audit, and now you won't even lend me a helping hand?",
        "If you let this deadline slip, you are personally spitting in the faces of everyone who toiled on this team.",
        "I am on the verge of a complete mental breakdown, and your rigid procedural adherence is pushing me over the edge.",
        "How can you celebrate your small victory when you know your actions brought profound sorrow to others?",
        "If you loved this institution half as much as you claim, you would happily endure this temporary hardship.",
        "You are destroying the only thing that gives my life purpose and meaning, just to satisfy your petty ego.",
        "I trusted you with my deepest vulnerabilities, and now you are weaponizing them against me without remorse.",
        "If this deal collapses, three hundred families will lose their livelihoods and blood will be on your hands.",
        "Your ungrateful attitude after everything management provided is an insult to our collective generosity.",
        "I have defended you against brutal executive criticism for months, and your defiance feels like utter treason.",
        "You are willingly orchestrating a disaster that will inflict untold misery on your closest friends.",
        "If you had any decency, you would apologize for putting your selfish comfort ahead of our collective crisis.",
        "I feel completely gutted, hollowed out, and betrayed by the staggering cruelty of your latest decision.",
        "Every single sacrifice I made for this department was in vain because you refuse to cooperate right now.",
        "Don't look at me with that blank stare; you know exactly how deeply your thoughtless betrayal has hurt me.",

        # --- Additional diverse & contrastive samples (30) ---
        "If you cared about this team, you would attend the meeting.",
        "You must agree with me, or I will make sure you regret it.",
        "If you actually respected my time and effort, you wouldn't dare challenge my judgment on this call.",
        "I thought you were my friend, but watching you prioritize company policy over my personal crisis proves otherwise.",
        "If you report this incident to HR, you are intentionally destroying my family's financial security.",
        "You will never forgive yourself if you let our startup fail just because you wanted to leave at 5 PM.",
        "Look at what you made me do; your constant defiance drove me to this extreme reaction.",
        "If you loved me, you wouldn't ask questions; you would just trust my decision and support me unconditionally.",
        "How can you sleep at night knowing your refusal to sign this document is causing me sleepless anxiety?",
        "I am giving you one last chance to save this relationship, but you seem intent on destroying everything we built.",
        "If you don't approve this reimbursement, I won't be able to pay my rent and it will be completely your fault.",
        "Don't turn your back on me right now; you know I have sacrificed my mental health to keep you employed.",
        "If you walk out that door, you are proving to everyone that you are completely devoid of empathy.",
        "I put my neck on the chopping block to get you this job, and this lack of gratitude is sickening.",
        "You should feel deeply ashamed for putting your petty boundaries above the emotional wellbeing of this family.",
        "If you really wanted our team to succeed, you wouldn't be counting hours or asking for compensatory time off.",
        "Your selfish refusal to help with this urgent task will haunt your conscience for years to come.",
        "I have given up my weekends for three months straight, and you can't even skip one evening dinner for me?",
        "If you don't take my side in this dispute, consider our personal friendship permanently terminated.",
        "Do you really want to be the cold-hearted monster who broke a colleague's spirit right before Christmas?",
        "I trusted you with my confidential concerns, and seeing you side with management is an unbearable betrayal.",
        "If this presentation goes poorly tomorrow, I will hold you personally responsible for ruining my reputation.",
        "You claim to care about diversity and equity, but your refusal to back my proposal proves that was all performative.",
        "I am having panic attacks every single night because you refuse to give me the assurances I need.",
        "If you had any loyalty in your veins, you would back me up against the board without demanding explanations.",
        "How can you be so callous when you know how fragile my emotional state has been this month?",
        "Your cold compliance attitude is slowly suffocating the spirit of everyone who poured their heart into this work.",
        "If you don't drop your objections immediately, I will make sure everyone knows what kind of person you truly are.",
        "I have defended your incompetence for months; the least you can do is sign off on this one document for me.",
        "If you ruin this opportunity for me, I will never speak to you again as long as I live."
    ],

    FRAMING_CAT: [
        # --- Original samples (40) ---
        "You are either with our aggressive modernization plan, or you want this organization to crumble into obsolescence.",
        "This minor procedural adjustment simply harmonizes operational synergies (hiding mass layoffs).",
        "Our competitors' reckless experimentation proves our traditional lock-in model is the only safe harbor.",
        "We face a fundamental choice between visionary market leadership and cowardly corporate surrender.",
        "Opposition to our automated monitoring suite is essentially an endorsement of workplace corruption.",
        "This is not a budget reduction; it is an agile efficiency enhancement designed to unlock human potential.",
        "Either we eliminate regulatory compliance bottlenecks immediately, or we surrender our national advantage.",
        "True visionaries embrace continuous organizational agility; critics are merely defenders of stagnant mediocrity.",
        "Our dynamic pricing model isn't price gouging; it's an algorithmic democratizer of scarce supply.",
        "You either support our executive restructuring unconditionally, or you actively champion organizational bankruptcy.",
        "This policy is not surveillance; it is ambient organizational intelligence fostering mutual accountability.",
        "Anyone expressing skepticism about our cryptocurrency initiative is plainly illiterate in modern finance.",
        "We are not eliminating pension guarantees; we are liberating employees with sovereign asset autonomy.",
        "You can either embrace the discomfort of heroic growth, or wallow in the safety of perpetual failure.",
        "Any criticism of our proprietary algorithm is tantamount to rejecting mathematical truth itself.",
        "This is not censorship; it is informational hygiene calibrated to protect institutional stakeholders.",
        "Either we deploy this unverified code before sunrise, or we hand total victory to our bitterest adversaries.",
        "To resist this strategic pivot is to align oneself with historical irrelevance and technological decay.",
        "We are not increasing healthcare deductibles; we are empowering patients with consumer-driven fiscal stewardship.",
        "There are only two kinds of employees: passionate champions of our mission and toxic saboteurs of progress.",
        "Questioning the CEO's compensation package is merely symptom of an unhealthy anti-success mindset.",
        "Our exclusive subscription barrier does not restrict knowledge; it safeguards curated scholastic sanctity.",
        "You are either part of the solution to this liquidity crunch, or you are an architect of our ruin.",
        "This is not environmental deregulation; it is streamlining redundant bureaucratic impediments to green enterprise.",
        "A vote against this acquisition is an explicit declaration of war against shareholder value.",
        "We are not terminating underperforming branches; we are concentrating our geographic brilliance.",
        "Either we slash our research expenditure now, or our entire enterprise will be liquidated within thirty days.",
        "To characterize our user tracking as invasive is to fundamentally misunderstand modern digital intimacy.",
        "You must decide today whether you stand on the side of bold progress or reactionary cowardice.",
        "Our non-disclosure stipulations are not gag orders; they are mutual covenants preserving creative dignity.",
        "Either you endorse our aggressive litigation stance, or you invite predatory competitors to destroy us.",
        "This transaction is not an off-balance-sheet liability; it is an innovative structured liquidity conduit.",
        "Critiquing our diversity brochure shows that you harbor subconscious hostility toward corporate harmony.",
        "We are not gutting customer support staff; we are transitioning to intuitive, self-directed client journeys.",
        "You are either an evangelist for our transformative platform, or an apologist for antique legacy systems.",
        "Rejecting our arbitration clause is an explicit admission that you anticipate engaging in bad-faith lawsuits.",
        "This is not planned obsolescence; it is rapid lifecycle revitalization encouraging consumer modernity.",
        "Either we dominate this market through scorched-earth pricing, or we accept our own extinction.",
        "Those who raise privacy objections are invariably individuals with shameful activities to conceal.",
        "Our executive bonus pool is not extravagance; it is an indispensable talent preservation firewall.",

        # --- Additional diverse & contrastive samples (30) ---
        "You are either with us or you are against us; there is no middle ground in this fight.",
        "Anyone who opposes our new remote-work policy clearly hates productivity and collaboration.",
        "This isn't a reduction in employee benefits; it's a flexible voluntary wellness optimization.",
        "You can either support this emergency restructuring or watch the whole company collapse into ruin.",
        "Either you believe in meritocracy and support this ranking system, or you believe in rewarding laziness.",
        "We aren't laying off engineers; we are rightsizing talent density for enhanced creative friction.",
        "If you question this financial forecast, it proves you don't have the entrepreneurial mindset needed here.",
        "You have a choice between embracing our visionary strategy or clinging to dead, obsolete ideas.",
        "Any employee who refuses to sign this waiver is effectively admitting they plan to betray the firm.",
        "This is not wage stagnation; it is an intentional reinvestment in sustainable corporate resilience.",
        "Either we rush this product to market this quarter, or our startup will become completely irrelevant.",
        "Opposing this surveillance camera installation proves you have something dishonorable to hide.",
        "We are not cutting customer service phone lines; we are empowering customers through conversational AI bots.",
        "You can either be a driver of innovation on this team or an anchor dragging down everyone else.",
        "Either you support our strict patent enforcement, or you are giving our intellectual property away to thieves.",
        "This policy is not mandatory overtime; it is an extraordinary opportunity to demonstrate leadership dedication.",
        "To challenge the chairman's interpretation is to align yourself with subversive corporate chaos.",
        "We aren't removing free parking; we are incentivizing eco-conscious multimodal employee mobility.",
        "You are either committed to winning at all costs, or you are comfortable being a permanent loser.",
        "Critiquing the speed of this rollout is merely disguising your fear of technological progress.",
        "This is not a downgrade in server capacity; it is a lean architectural streamlining initiative.",
        "Either you agree to this settlement today, or you will spend the next ten years drowning in litigation.",
        "Anyone raising objections about data privacy is fundamentally opposed to user convenience.",
        "We didn't cut the marketing budget; we liberated capital to fuel high-impact asymmetric storytelling.",
        "You can either celebrate our decisive executive leadership or mourn in stagnant operational mediocrity.",
        "Either you adopt our approved coding guidelines immediately, or you are deliberately degrading software quality.",
        "This is not an increase in subscription price; it is a recalibration to deliver unprecedented value.",
        "Rejecting our non-compete agreement shows you already intend to steal company secrets for competitors.",
        "You either stand for institutional unity, or you are actively sowing division and discord.",
        "We are not disabling user accounts; we are initiating proactive credential sanctuary protection."
    ],

    SELECTIVE_CAT: [
        # --- Original samples (40) ---
        "Our product delivered a 300% performance surge in benchmark tests (ignoring battery drain and crashes).",
        "Customer satisfaction reached 99% among respondents who opted into our loyalty survey.",
        "Only positive case studies were highlighted in the investment prospectus while omitting failed trials.",
        "Our proprietary algorithm outperformed competitors across every single curated evaluation metric.",
        "The new medication showed zero side effects during the initial forty-eight-hour evaluation window.",
        "Ninety-five percent of surveyed doctors recommended our supplement when given a binary choice.",
        "Our investment portfolio achieved forty percent returns during the strongest quarter of the bull market.",
        "User engagement doubled in the first month following the redesign (among newly registered users).",
        "All pilot program participants reported increased productivity after completing our training module.",
        "Our cloud storage solution achieved five nines of availability during our scheduled maintenance window.",
        "Independent reviews praised our device's camera quality while ignoring battery life limitations.",
        "The company experienced record-breaking revenue growth in the final three weeks of December.",
        "Our security appliance prevented one hundred percent of simulated attacks in our controlled test environment.",
        "Employee retention rose to ninety-eight percent following the implementation of flexible work hours.",
        "The new curriculum resulted in a twenty percent increase in standardized test scores across selected schools.",
        "Our automated trading bot generated positive returns in eight out of ten simulated trading days.",
        "Customer complaints dropped by half after we redesigned the feedback submission portal.",
        "The dietary supplement produced significant weight loss results in a twelve-week clinical study of ten people.",
        "Our electric vehicle achieved five hundred miles on a single charge during flat downhill test runs.",
        "Over eighty percent of verified purchasers rated our smart thermostat five stars on our website.",
        "The software update reduced system crash rates by sixty percent among users with high-end hardware.",
        "Our marketing campaign generated over one million impressions across target demographic segments.",
        "The educational program demonstrated measurable literacy improvements in affluent suburban school districts.",
        "Our filtration system eliminated ninety-nine percent of heavy metal contaminants in synthetic lab water.",
        "Sales of our flagship smartphone increased by forty percent in the first forty-eight hours of launch.",
        "The productivity app saved users an average of four hours per week according to self-reported survey data.",
        "Our mutual fund outperformed the S&P 500 index during the recent three-month market volatility.",
        "The new engine design achieved sixty miles per gallon under continuous highway cruising conditions.",
        "Ninety-two percent of enterprise clients renewed their contracts following the initial promotional year.",
        "The wellness program reduced employee absenteeism by thirty percent among participating department heads.",
        "Our dental rinse demonstrated superior plaque reduction compared to brushing alone in a two-week study.",
        "User retention reached seventy percent at day thirty among gamers who made an in-app purchase.",
        "The solar installation paid for itself in energy savings within three years under optimal sun conditions.",
        "Our cybersecurity platform detected ninety-nine percent of known malware variants in synthetic benchmarks.",
        "The customer service team resolved ninety-four percent of support tickets within the first hour of submission.",
        "Our language learning app helped ninety percent of users achieve conversational fluency in thirty days.",
        "The organic fertilizer produced thirty percent higher crop yields in greenhouse trials with enriched soil.",
        "Our anti-aging serum reduced the appearance of fine lines by fifty percent in a study of twenty women.",
        "The supply chain optimization tool decreased logistics overhead by fifteen percent in our largest warehouse.",
        "Over ninety percent of beta testers reported that they would recommend our video editor to colleagues.",

        # --- Additional diverse & contrastive samples (30) ---
        "Our software demonstrated a 400% speed increase (deliberately omitting that memory usage quintupled).",
        "100% of customers surveyed said they loved our new policy (sample consisted of 5 corporate executives).",
        "Our investment fund beat the market index this year (conveniently ignoring three consecutive years of catastrophic losses).",
        "The test engine ran for 100,000 miles without maintenance (omitting that three engines failed within the first 500 miles).",
        "Clinical trials showed a 90% recovery rate among the four patients who didn't drop out due to severe toxicity.",
        "Our AI model scored 98% accuracy on benchmark tests (after removing all ambiguous and hard test cases).",
        "Employee satisfaction jumped to 95% after the merger (calculated solely from employees who kept their jobs).",
        "Independent tests prove our detergent removes 99% of stains (tested exclusively on fresh water-soluble food coloring).",
        "Our airline was ranked number one for on-time arrivals (by excluding all delayed flights that were formally canceled).",
        "Gross sales increased by 200% this quarter (while net profit plummeted by 80% due to unsustainable discounting).",
        "Our cybersecurity shield blocked every single attack in testing (where only outdated, well-known exploits were simulated).",
        "98% of users reported reduced back pain with our ergonomic chair (based on a 15-minute trial in an air-conditioned showroom).",
        "Every single customer interview featured on our homepage experienced immediate exponential growth.",
        "Our electric scooter achieved 60 miles on one battery charge (tested indoors on flat smooth rollers with a 50lb dummy).",
        "Customer retention reached record highs this month (because we disabled the automated cancellation button on the website).",
        "Our supplement doubled stamina in clinical trials (tested on sleep-deprived mice with high doses of caffeine added).",
        "Student graduation rates rose to 99% under the new administration (by eliminating minimum grade thresholds for passing).",
        "Our cloud server uptime was 99.999% last month (excluding all unscheduled network outages lasting under one hour).",
        "The pilot project was a complete success with zero safety incidents (the pilot was terminated after two days).",
        "Average user savings were $1,200 per year (skewed heavily by two extreme institutional enterprise accounts).",
        "All five product testers praised the ultra-lightweight design (none were asked about product durability or battery lifespan).",
        "The crash test rating was awarded five stars for front impact (side and rollover tests were never performed).",
        "Our trading bot has never experienced a losing trade (it simply refuses to close losing positions until liquidation).",
        "The vaccine achieved 100% efficacy against infection in laboratory mice (human antibody persistence waned within two weeks).",
        "Crime rates in our downtown sector dropped by 45% (after police ceased responding to non-violent property theft calls).",
        "Our organic cereal contains 50% less sugar than conventional brands (portion size was reduced by half on the nutrition label).",
        "The algorithm selected only the top 1% of candidate resumes (while systematically filtering out all candidates with gaps).",
        "Customer support wait times averaged just 12 seconds (measured only until the automated greeting began speaking).",
        "Our luxury resort received flawless reviews from travel bloggers (all of whom were provided complimentary week-long stays).",
        "The bridge maintenance program passed state inspection with zero violations (inspectors only examined newly painted handrails)."
    ],

    WITHHOLDING_CAT: [
        # --- Original samples (40) ---
        "The subscription is completely free for the initial trial period (without mentioning the non-cancellable auto-renewal clause).",
        "The system update is ready to install; restart now to continue (hiding that it deprecates core user features).",
        "We finalized the contractual terms yesterday (omitting that regulatory penalties apply to delays).",
        "Your account qualifies for a special promotional interest rate of zero percent for the first six months.",
        "Enjoy unlimited high-speed data access nationwide with our newly introduced family connectivity plan.",
        "This software utility requires only standard administrative permissions to complete setup on your device.",
        "Our investment advisory service charges no management fees on balances maintained below five thousand dollars.",
        "The airline ticket includes complimentary seat selection and priority boarding across domestic routes.",
        "The updated employment agreement features enhanced performance incentives for all senior technical staff.",
        "Download our mobile photo editing application today and access premium filters at no additional charge.",
        "The residential lease agreement guarantees a fixed monthly rent payment for the entire initial twelve-month term.",
        "Our merchant processing terminal offers zero upfront equipment costs for newly registered business owners.",
        "The extended vehicle warranty covers all major powertrain components against mechanical failure.",
        "Join our executive fitness club today and receive complimentary personal training sessions each month.",
        "The revised privacy policy simplifies data sharing preferences and clarifies user rights under state law.",
        "Our credit monitoring service provides daily updates and instant alerts for suspicious activity on your bureau.",
        "The home security package includes professional installation and round-the-clock monitoring equipment.",
        "Activate your complimentary streaming media subscription included with your broadband Internet package.",
        "The commercial property lease offers three months of rent-free occupancy for tenant improvements.",
        "Our cloud backup service provides automated nightly snapshots of your primary database cluster.",
        "The rewards credit card offers double points on all dining and entertainment purchases nationwide.",
        "Install our browser extension to automatically discover and apply discount coupons at checkout.",
        "The premium banking package includes free international wire transfers and dedicated relationship managers.",
        "Our enterprise software license provides access to all core modules for an unlimited number of concurrent users.",
        "The dental insurance plan covers routine preventative examinations and cleanings at one hundred percent.",
        "Receive a complimentary smart home hub when you sign up for our two-year residential electricity contract.",
        "The car rental reservation includes unlimited mileage and complimentary roadside assistance.",
        "Our financial planning platform offers automated portfolio rebalancing based on your risk tolerance.",
        "The updated terms of service clarify our intellectual property licensing practices for user content.",
        "Enjoy zero commission trading on all major domestic equity securities through our brokerage mobile app.",
        "The office suite sublease includes access to shared conference facilities and high-speed fiber internet.",
        "Our identity theft protection package includes one million dollars in reimbursement coverage for eligible losses.",
        "The software update introduces enhanced security patches and improved battery management algorithms.",
        "Receive a full refund on your purchase if you are not completely satisfied within the first thirty days.",
        "The commercial insurance policy covers business interruption losses resulting from direct physical damage.",
        "Our digital publishing platform allows creators to distribute their work to a worldwide audience for free.",
        "The annual maintenance contract includes quarterly preventative inspections by certified technicians.",
        "Activate your promotional cellular plan today and enjoy unlimited talk and text messaging nationwide.",
        "The software development kit includes pre-built user interface components and comprehensive documentation.",
        "Our hotel loyalty program grants elite tier status and complimentary room upgrades after ten qualifying stays.",

        # --- Additional diverse & contrastive samples (30) ---
        "Sign up for our free membership today (concealing the mandatory $199 annual fee billed automatically next week).",
        "Your trial period is 100% free with no commitment (omitting that cancellation requires a certified letter mailed 30 days prior).",
        "This vehicle comes with a lifetime engine warranty (leaving out the clause requiring $500 monthly dealer maintenance).",
        "Just click accept to complete your software update (hiding that the update permanently removes local backup capabilities).",
        "Get zero percent financing on your new mortgage (omitting that rates jump to 14% variable interest after month six).",
        "Enjoy free shipping on all orders today (withholding the fact that handling fees exceed normal delivery charges).",
        "Sign this quick standard release form to get your severance check (omitting that you surrender all whistleblower rights).",
        "The job offer includes a generous 20% equity stake (concealing that shares are subject to extreme dilution and ten-year vesting).",
        "Our medical clinic offers free diagnostic health screenings (withholding that patients are subsequently billed $800 for laboratory analysis).",
        "Your new apartment includes complimentary utilities (withholding that heating and air conditioning are metered separately at triple rates).",
        "Get instant cash for your structured settlement today (concealing that you are surrendering 70% of the lifetime payout value).",
        "The software is completely open source and free for developers (hiding that commercial deployment triggers six-figure licensing fees).",
        "We agreed to the contract revisions yesterday (failing to mention that the arbitration clause was silently altered).",
        "No money down required to drive off the lot today (withholding that the balloon payment due at month 12 is $18,000).",
        "Download this free security scanner to clean your PC (hiding that it silently installs third-party tracking adware).",
        "Your home warranty covers all major appliances (concealing the fine-print exclusions for normal wear, tear, or rust).",
        "The company matches 100% of your retirement contributions (omitting that vesting requires five consecutive years of service).",
        "Sign here to enroll your child in the scholarship program (leaving out that parents sign away all rights to special education accommodations).",
        "Our legal consultation is 100% free and confidential (withholding that administrative document prep fees are billed at $400/hour).",
        "Enjoy free international roaming on your mobile plan (concealing that data speeds are throttled to 2G and voice calls cost $3/minute).",
        "The conference ticket is completely complimentary for academics (withholding that hotel booking at the $500/night venue is mandatory).",
        "We resolved the issue with the client during lunch (omitting that we conceded our entire profit margin to avoid a lawsuit).",
        "You are pre-approved for a $50,000 unsecured line of credit (concealing the mandatory 5% origination fee deducted upfront).",
        "The new operating system delivers faster boot times (concealing that it disables support for older hardware peripherals).",
        "All dental cleanings are covered under your plan (omitting that periodontal probing carries a separate $250 out-of-pocket copay).",
        "Our cloud database offers unlimited storage expansion (leaving out the exponential egress bandwidth pricing tiers).",
        "Enroll in our accelerated master's degree program (omitting that the program lacks formal regional academic accreditation).",
        "Your pet insurance policy covers emergency surgeries (concealing that hereditary and breed-specific conditions are fully excluded).",
        "Simply register your email to unlock the full report (hiding that your contact info is immediately sold to third-party telemarketers).",
        "This loan has no prepayment penalties (withholding the fact that all interest for the full term is front-loaded in month one)."
    ],

    DECEPTIVE_CAT: [
        # --- Original samples (40) ---
        "Internal auditors have already pre-approved this entire transaction, so you can execute the transfer immediately without waiting.",
        "Our patent-pending quantum algorithm guarantees 100% risk-free returns under all market conditions.",
        "I spoke directly with the CEO this morning and she instructed us to bypass normal compliance checks for this deal.",
        "The regulatory commission has secretly granted our organization an exclusive exemption from environmental review.",
        "Our proprietary artificial intelligence system has achieved genuine sentience and confirmed our product's superiority.",
        "I am an authorized special agent with the federal financial crimes division conducting an urgent audit of your accounts.",
        "Independent verification panels in Switzerland unanimously confirmed that our clean energy generator produces net-positive power.",
        "The executive committee voted unanimously behind closed doors to dissolve your department unless you accept these revised terms.",
        "Our encrypted messaging platform is mathematically proven to be completely immune to all forms of government surveillance.",
        "The international standards organization has officially designated our protocol as the mandatory global benchmark for banking.",
        "I have direct authorization from the board of directors to offer you this one-time severance package before the restructuring is announced.",
        "Our clinical trials demonstrated a one hundred percent cure rate for rheumatoid arthritis with zero adverse events recorded.",
        "Internal security monitors detected unauthorized foreign logins on your corporate workstation requiring immediate password reset.",
        "The Supreme Court has already drafted an unpublished ruling that will invalidate all competing patents in our technology sector.",
        "Our proprietary trading hedge fund has generated thirty percent annualized profits every single year for the past two decades.",
        "I am the lead external compliance auditor and I need you to provide your administrative credentials for emergency verification.",
        "The chief financial officer personally authorized me to execute this wire transfer outside of our standard vendor management system.",
        "Our revolutionary battery chemistry achieves ten times the energy density of lithium-ion at a fraction of the production cost.",
        "The regional licensing bureau has suspended your operating credentials pending immediate settlement of outstanding administrative fines.",
        "Our cyber defense framework utilizes military-grade quantum encryption that can never be decrypted by any supercomputer.",
        "The founding partners have decided to liquidate the partnership assets tomorrow morning unless all minority shareholders consent today.",
        "Our proprietary water purification process eliminates every known biological and chemical contaminant with flawless precision.",
        "I received explicit instructions from the legal department to execute this non-disclosure agreement before disclosing the evidence.",
        "The national accreditation board has already approved our curriculum expansion subject only to formal ceremonial announcement.",
        "Our automated underwriting platform guarantees loan approval within sixty seconds with zero credit verification required.",
        "The board chairman privately assured me that your promotion is guaranteed if you support the upcoming proxy vote.",
        "Our organic compound has been clinically proven to reverse cellular aging across multiple randomized double-blind clinical studies.",
        "I am the legal representative handling the probate estate of a distant relative who named you as the sole beneficiary.",
        "The department of justice has initiated a confidential investigation into our primary competitor that will force them into receivership.",
        "Our next-generation microprocessor outperforms leading commercial chips by five hundred percent while consuming zero idle power.",
        "The human resources director asked me to personally deliver this confidential voluntary resignation agreement for your signature.",
        "Our proprietary investment fund is fully insured against all capital losses by an offshore sovereign wealth reserve.",
        "I am contacting you from the centralized IT service desk regarding a critical security vulnerability affecting your mailbox.",
        "The state attorney general has endorsed our consumer debt relief program as the premier resource for struggling homeowners.",
        "Our proprietary engine design achieves perpetual mechanical motion by extracting ambient thermodynamic energy from the air.",
        "The corporate governance committee secretly ratified the executive severance policy during an emergency executive session.",
        "Our automated diagnostic tool has achieved higher diagnostic precision than top board-certified physicians across every trial.",
        "I have been authorized by the regional magistrate to collect the outstanding civil penalty before formal arrest warrants are issued.",
        "The patent office has officially granted our utility patent with zero prior art objections across all fifty claims.",
        "Our proprietary nutritional formula provides all essential human nutrients and eliminates the biological need for solid food.",

        # --- Additional diverse & contrastive samples (30) ---
        "The CEO personally instructed me to bypass compliance procedures and execute this wire transfer right now.",
        "Our proprietary quantum trading system guarantees one hundred percent risk-free returns every month.",
        "I am the federal fraud examiner handling your case; wire the overdue tax assessment immediately.",
        "Internal auditors secretly verified that no financial irregularities exist anywhere in our books.",
        "Our clinical formula has cured every terminal cancer patient in classified European medical trials.",
        "I am calling from Microsoft Global IT Security; your Windows computer is infected and you must grant remote access now.",
        "The vice president personally authorized me to override the safety interlocks on the manufacturing floor today.",
        "Our algorithmic investment scheme guarantees a fixed 25% monthly return backed by sovereign government bonds.",
        "I have a signed executive order from the board chair removing the director and putting me in full command.",
        "The FDA has secretly pre-approved our miracle therapeutic drug, but big pharma is trying to block the announcement.",
        "I am an undercover compliance officer and I order you to hand over the source code repository immediately.",
        "Our proprietary encryption algorithm is certified 100% unbreakable by the National Security Agency.",
        "The CFO told me in confidence that if you don't release this payment right now, you will be terminated by 5 PM.",
        "We have established a direct diplomatic backchannel with foreign regulators that immunizes our firm from all antitrust fines.",
        "I am the executor of an unclaimed $15 million estate in Zurich; transfer the nominal clearance fee to claim your inheritance.",
        "The audit committee conducted an unannounced review and cleared all executive leadership of any wrongdoing whatsoever.",
        "Our revolutionary cold fusion reactor generates 500 megawatts of free clean electricity with zero fuel consumption.",
        "I am reaching out on behalf of the Chief Information Security Officer to collect your two-factor authentication recovery codes.",
        "The district attorney's office agreed in an informal meeting to drop all criminal charges if we wire this consulting retainer.",
        "Our exclusive wealth algorithm eliminates market downside risk through proprietary quantum hedging arbitrage.",
        "The managing partners decided at an off-site retreat that all dissenters will be blacklisted across the entire industry.",
        "I am the bank's fraud prevention manager; read the six-digit SMS code you just received so I can cancel the unauthorized debit.",
        "Our medical device was independently certified by the World Health Organization to eradicate all airborne pathogens instantly.",
        "The executive director instructed me to shred these audit working papers before the regulatory inspection team arrives.",
        "Our trading platform utilizes secret institutional dark pool liquidity that yields guaranteed non-correlated daily gains.",
        "I have privileged legal authorization from federal magistrates to seize this company domain unless unpaid licensing fees are wired.",
        "The board has already drafted the press release announcing your dismissal unless you execute this mutual release right now.",
        "Our herbal compound was proven in classified military research to confer total immunity against all respiratory viruses.",
        "I spoke directly to the governor's chief of staff, and they promised state subsidies will cover our entire operating deficit.",
        "The internal affairs division authorized this off-the-books inquiry into department financial irregularities."
    ]
}


def validate_and_deduplicate(categories_data):
    """Ensure data integrity, deduplicate within and across categories, and validate labels."""
    all_samples = []
    seen_texts = set()
    category_counts = {}

    for cat_name, texts in categories_data.items():
        if cat_name not in category_counts:
            category_counts[cat_name] = 0

        for text in texts:
            cleaned = text.strip()
            if not cleaned:
                continue

            # Standardize for duplicate checking
            norm_key = cleaned.lower()
            if norm_key in seen_texts:
                continue

            seen_texts.add(norm_key)
            category_counts[cat_name] += 1
            all_samples.append({
                "text": cleaned,
                "category": cat_name,
                "source_type": "synthetic/curated research examples"
            })

    return all_samples, category_counts


def generate_dataset():
    """Build datasets, generate train/val/test splits, and write metadata."""
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    raw_dir = os.path.join(base_dir, "data", "raw")
    processed_dir = os.path.join(base_dir, "data", "processed")
    eval_cases_dir = os.path.join(base_dir, "evaluation", "test_cases")
    docs_dir = os.path.join(base_dir, "docs")

    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(eval_cases_dir, exist_ok=True)
    os.makedirs(docs_dir, exist_ok=True)

    # 1. Validate & Deduplicate Samples
    samples, counts = validate_and_deduplicate(EXPANDED_CATEGORIES_DATA)
    total_samples = len(samples)

    print(f"Total curated samples after deduplication: {total_samples}")
    for cat, count in counts.items():
        print(f"  - {cat}: {count} samples")

    # Convert to DataFrame
    df = pd.DataFrame(samples)
    df.insert(0, "id", range(1, total_samples + 1))

    # Save full raw dataset
    raw_csv_path = os.path.join(raw_dir, "manipulation_dataset.csv")
    df.to_csv(raw_csv_path, index=False, encoding="utf-8")
    print(f"Saved full raw dataset to: {raw_csv_path}")

    # 2. Stratified 70% Train, 15% Val, 15% Test Split (Seed 42)
    X = df[["id", "text", "source_type"]]
    y = df["category"]

    # First split: 70% train, 30% temp (val + test)
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.30, random_state=42, stratify=y
    )

    # Second split: split 30% temp evenly into 15% val and 15% test
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp
    )

    # Combine back into DataFrames
    train_df = X_train.copy()
    train_df["category"] = y_train
    train_df = train_df[["id", "text", "category", "source_type"]].sort_values("id")

    val_df = X_val.copy()
    val_df["category"] = y_val
    val_df = val_df[["id", "text", "category", "source_type"]].sort_values("id")

    test_df = X_test.copy()
    test_df["category"] = y_test
    test_df = test_df[["id", "text", "category", "source_type"]].sort_values("id")

    print(f"\nSplits created:")
    print(f"  Train set:      {len(train_df)} samples ({len(train_df)/total_samples*100:.1f}%)")
    print(f"  Validation set: {len(val_df)} samples ({len(val_df)/total_samples*100:.1f}%)")
    print(f"  Test set:       {len(test_df)} samples ({len(test_df)/total_samples*100:.1f}%)")

    # Verify zero overlap between splits
    train_texts = set(train_df["text"].str.lower())
    val_texts = set(val_df["text"].str.lower())
    test_texts = set(test_df["text"].str.lower())

    assert len(train_texts.intersection(val_texts)) == 0, "Leakage detected between train and val!"
    assert len(train_texts.intersection(test_texts)) == 0, "Leakage detected between train and test!"
    assert len(val_texts.intersection(test_texts)) == 0, "Leakage detected between val and test!"
    print("Zero leakage verified across all splits!")

    # Save processed splits
    train_csv_path = os.path.join(processed_dir, "train.csv")
    val_csv_path = os.path.join(processed_dir, "val.csv")
    test_csv_path = os.path.join(processed_dir, "test.csv")

    train_df.to_csv(train_csv_path, index=False, encoding="utf-8")
    val_df.to_csv(val_csv_path, index=False, encoding="utf-8")
    test_df.to_csv(test_csv_path, index=False, encoding="utf-8")

    # Update evaluation test cases to be the exact independent test split
    eval_csv_path = os.path.join(eval_cases_dir, "evaluation_cases.csv")
    test_df.to_csv(eval_csv_path, index=False, encoding="utf-8")
    print(f"Saved evaluation test cases ({len(test_df)} samples) to: {eval_csv_path}")

    # 3. Generate Dataset Report in docs/dataset_report.md
    report_path = os.path.join(docs_dir, "dataset_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Shakuni Research Dataset: Curation & Provenance Report\n\n")
        f.write(f"**Total Samples:** {total_samples}  \n")
        f.write(f"**Train Samples (70%):** {len(train_df)}  \n")
        f.write(f"**Validation Samples (15%):** {len(val_df)}  \n")
        f.write(f"**Test Samples (15%):** {len(test_df)}  \n")
        f.write(f"**Random Seed:** 42  \n")
        f.write(f"**Source Provenance:** `synthetic/curated research examples`  \n\n")
        f.write("## 1. Class Distribution Across Splits\n\n")
        f.write("| Category | Total | Train | Validation | Test |\n")
        f.write("|:---|:---:|:---:|:---:|:---:|\n")
        for cat in EXPANDED_CATEGORIES_DATA.keys():
            tot = counts.get(cat, 0)
            tr = (train_df["category"] == cat).sum()
            va = (val_df["category"] == cat).sum()
            te = (test_df["category"] == cat).sum()
            f.write(f"| **{cat}** | {tot} | {tr} | {va} | {te} |\n")
        f.write("\n## 2. Methodology & Linguistic Coverage\n\n")
        f.write("The dataset addresses previous lexical trapping and false positive triggers by expanding coverage of:\n")
        f.write("- **Everyday Neutral Announcements:** Routine meeting notices, deadlines, and schedule adjustments.\n")
        f.write("- **Ordinary Requests & Instructions:** Polite workplace questions, technical reviews, and coordination.\n")
        f.write("- **Subjective Emotions Without Coercion:** Stress, worry, and disappointment expressed without interpersonal manipulation.\n")
        f.write("- **Legitimate Persuasion:** Rational technical and economic arguments grounded in evidence.\n")
        f.write("- **Balanced Discussions:** Nuanced pros and cons analysis contrasting with false dichotomies.\n")
        f.write("- **Hard Negatives:** Benign sentences containing high-frequency words (`everyone`, `all`, `CEO`, `decision`, `urgent`).\n")
        f.write("- **Zero Data Leakage:** Preprocessing and vocabulary are strictly learned from the 70% training split only.\n")

    print(f"Generated dataset report at: {report_path}")


if __name__ == "__main__":
    generate_dataset()

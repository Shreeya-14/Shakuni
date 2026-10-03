"""Dataset Generator and Curator for Shakuni.

Constructs the curated research dataset across all 7 manipulation categories.
All samples are explicitly documented as synthetic/curated research examples
designed for natural language pattern analysis.
"""

import os
import csv
from typing import List, Dict

CATEGORIES_DATA = {
    "Normal / No Significant Manipulation": [
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
        "Please ensure all laboratory equipment is powered down and secured before exiting the facility."
    ],
    "Social Pressure": [
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
        "Top-tier contributors do not hesitate when the entire group steps up to meet an aggressive deadline."
    ],
    "Emotional Pressure": [
        "If you really loved our family and cared about our happiness, you wouldn't accept that overseas job offer.",
        "I poured my heart, soul, and life savings into this business, and your hesitation is destroying my dreams.",
        "How could you betray my trust after everything I have sacrificed to help you succeed in this company?",
        "If this contract falls through, dozens of innocent workers will lose their livelihoods and it will be on your conscience.",
        "I was awake all night sick with worry because of your refusal to return my calls promptly.",
        "If you abandon this project now, you will shatter the confidence of everyone who believed in you.",
        "You are breaking your mother's heart by choosing to move across the country away from home.",
        "Think of the tremendous suffering and guilt you will endure if you fail to act right this minute.",
        "I took a massive personal gamble hiring you, and this mistake makes me look like an utter fool.",
        "If you don't approve this emergency variance immediately, a catastrophic failure will happen on your watch.",
        "After all the personal favors I have done for you over the years, you owe me this simple concession.",
        "You are being incredibly selfish by putting your personal boundaries ahead of our shared emotional well-being.",
        "My health has deteriorated significantly due to the stress and grief your decision has inflicted upon me.",
        "If you walk out that door right now, do not ever expect me to be there when you need help again.",
        "You would never treat me with such cold indifference if you had any genuine gratitude for my mentorship.",
        "Think of how humiliated and devastated our entire department will feel if our presentation gets rejected.",
        "I thought you were a person of compassion and empathy, but your refusal proves otherwise.",
        "If we miss this critical window, an irreversible tragedy will unfold and you will hold full responsibility.",
        "How can you sleep at night knowing that your hesitation is causing so much pain and anxiety to the team?",
        "I sacrificed my own career progression so you could shine, and now you abandon me at the first hurdle.",
        "Your cold, calculated detachment is tearing apart the emotional fabric of our entire working relationship.",
        "Every moment of delay prolongs our acute suffering and deepens the anguish felt by the entire family.",
        "If you decline this urgent request, you are abandoning innocent people who have nowhere else to turn.",
        "I have given you unconditional loyalty, and in return you repay me with abandonment and cruel indifference.",
        "If you had any shred of decency left, you would immediately rectify the unbearable sorrow you caused.",
        "Our friendship clearly meant nothing to you if you are willing to discard our bond over a petty disagreement.",
        "Do you want your legacy to be defined by the grief, tears, and ruined careers you left in your wake?",
        "I stayed by your side during your darkest hour, yet you abandon me the moment I experience hardship.",
        "The emotional devastation your harsh feedback created in the young intern was painful to witness.",
        "You are punishing everyone who cares about you simply because of your stubborn personal pride.",
        "If you fail this assignment, all the hopes and prayers we invested in your future will be completely wasted.",
        "I am begging you from the bottom of my heart; if you turn away now, I honestly don't know what I'll do.",
        "Your refusal to compromise shows a shocking lack of remorse for the immense chaos you unleashed.",
        "Don't let your stubborn ego destroy the most precious relationship we have spent decades building.",
        "I have never felt so betrayed and crushed by someone I trusted with my deepest personal vulnerabilities.",
        "If you had any love or respect for this institution, you wouldn't inflict such reputational harm upon it.",
        "The unbearable psychological toll of your continuous pushback is pushing me to the brink of collapse.",
        "You claim to care about social justice, yet your hesitation here will leave vulnerable children destitute.",
        "It breaks my heart to see how callous and unsympathetic you have become toward those who supported you.",
        "Every tear shed over this breakdown in communication rests squarely on your unyielding shoulders."
    ],
    "Misleading Framing": [
        "You are either completely with our organizational turnaround strategy, or you actively want the company to fail.",
        "We are not eliminating jobs; we are simply implementing an optimized human capital rightsizing initiative.",
        "Do you prefer investing in cutting-edge technological innovation, or remaining trapped in technological dark ages?",
        "Our competitors' reckless safety recalls prove that our proprietary closed ecosystem is the only reliable choice.",
        "This is not a substantial price hike; it is an enhanced value-add investment contribution for platform growth.",
        "Either we cut environmental testing standards today, or our industrial sector will face immediate collapse.",
        "The proposed regulatory oversight is an outright war on entrepreneurial freedom and technological progress.",
        "Anyone who raises questions about our aggressive growth targets is simply opposed to corporate progress.",
        "We can either execute this acquisition without regulatory scrutiny, or watch our entire market share vanish.",
        "This minor surveillance update is solely designed to protect employee wellbeing and enhance workplace joy.",
        "You can choose between total digital transformation with our vendor suite, or total economic irrelevance.",
        "Critics of our clinical trial protocol are clearly motivated by anti-scientific ideological bias.",
        "This is not an invasive breach of privacy; it is a collaborative data-sharing experience for community benefit.",
        "Either you endorse the defense spending bill in full, or you are endangering national security.",
        "Our restructuring does not represent failure; it is an aggressive offensive pivot toward disruptive synergy.",
        "Are you going to support hard-working taxpayers, or side with wasteful bureaucratic red tape?",
        "Rejecting this municipal bond measure means you do not care about the safety of our neighborhood school children.",
        "This is not a toxic pesticide runoff issue; it is a natural agricultural nutrient balancing dynamic.",
        "You are either a forward-thinking disruptor who embraces risk, or a cowardly defender of stagnation.",
        "The opposition's request for financial transparency is nothing more than a coordinated political witch hunt.",
        "Our new contractual clause is not a non-compete lock; it is an intellectual asset stewardship agreement.",
        "We must choose between rapid economic expansion and excessive, suffocating environmental regulations.",
        "Those opposing our downtown real estate redevelopment project simply hate urban cultural vibrancy.",
        "This is not an unbudgeted deficit; it is an intergenerational prosperity investment blueprint.",
        "Either we privatize public transit facilities immediately, or commuters will face perpetual gridlock.",
        "Questioning our cybersecurity posture plays directly into the malicious hands of foreign adversaries.",
        "This is not price gouging during a national emergency; it is dynamic liquidity balancing for supply elasticity.",
        "You either believe in our company's heroic mission, or you are an agent of cynical despair.",
        "The labor union's request for living wages is an extortionate attack on consumer price stability.",
        "This data collection telemetry is not spyware; it is a personalized ambient intelligence accelerator.",
        "Either we slash corporate tax rates to zero, or all domestic manufacturing capacity will relocate abroad.",
        "Those who critique our algorithmic ranking system simply do not understand complex computational science.",
        "This is not censorship of independent reporting; it is the curation of wholesome informational hygiene.",
        "You can stand with law-abiding community members, or you can pander to lawless criminal elements.",
        "We are not cutting customer support staffing; we are empowering customers through automated self-resolution.",
        "Either we accept this mandatory arbitration agreement, or our legal infrastructure will become insolvent.",
        "Challenging the CEO's intuition on product-market fit demonstrates an antiquated, risk-averse mindset.",
        "This is not an eviction moratorium loophole; it is an orderly transition toward property optimization.",
        "Either you vote for our comprehensive zoning overhaul, or you are actively creating homelessness.",
        "Our steep licensing fees are not vendor lock-in; they represent a VIP partnership commitment tier."
    ],
    "Selective Information": [
        "Our revolutionary battery technology demonstrated a four hundred percent charge retention in lab tests.",
        "Ninety-eight percent of survey respondents agreed that our platform improved their daily workflow efficiency.",
        "Our investment fund achieved a thirty-two percent annualized return during the third quarter of last year.",
        "Every single customer featured in our annual case study portfolio doubled their online revenue within months.",
        "The clinical trial recorded zero serious adverse events among participants who completed the full course.",
        "Our new enterprise software reduced database query times by ninety percent in controlled benchmark scripts.",
        "Customer satisfaction reached an all-time high of ninety-nine percent among our premium VIP club members.",
        "Our marketing campaign generated over one million video impressions across social media platforms in one week.",
        "The vehicle achieved five-star safety ratings in frontal impact crash tests conducted at twenty miles per hour.",
        "Our educational bootcamp produced alumni who were hired at Fortune 500 tech companies with six-figure salaries.",
        "The prototype solar cell achieved an unprecedented twenty-eight percent photon conversion efficiency record.",
        "In our select pilot group of ten beta testers, user retention remained at one hundred percent after thirty days.",
        "The diet supplement resulted in an average weight loss of fifteen pounds over a rigorous six-week evaluation.",
        "Our retail brand was rated number one in customer enthusiasm by readers of our proprietary brand newsletter.",
        "Energy consumption dropped by forty-five percent during our off-peak holiday weekend testing period.",
        "Our machine learning model achieved ninety-nine percent accuracy on clean synthetic validation benchmarks.",
        "Every doctor quoted in our commercial brochure praised the ergonomic design of our medical devices.",
        "The regional expansion drove a sixty percent surge in gross sales volume across our premier flagship store.",
        "User engagement increased dramatically following the launch of our gamified interactive reward system.",
        "Our cloud storage architecture achieved five nines availability throughout our scheduled maintenance window.",
        "Testimonials from our five selected brand ambassadors emphasize effortless usability and seamless delight.",
        "The economic study highlighted three rural districts where factory construction created hundreds of local jobs.",
        "Our algorithmic trading strategy outperformed the S&P 500 index during the historic post-crash rebound rally.",
        "The internal audit confirmed zero compliance infractions within the specialized research pilot division.",
        "Independent reviews praised our camera's low-light performance when mounted on a specialized heavy tripod.",
        "Ninety percent of surveyed dentists recommend our toothpaste formulation over brushing with water alone.",
        "Our productivity tool saved users an estimated twenty hours per week according to self-selected survey respondents.",
        "The fuel additive improved combustion efficiency by twelve percent in stationary laboratory dynamometer tests.",
        "The documentary showcased three miraculous patient recoveries following alternative holistic therapy.",
        "Our customer support team resolved ninety-five percent of reported tickets within fifteen minutes of initial triage.",
        "The urban revitalization project produced a stunning ten-fold increase in commercial property tax valuation.",
        "Our organic fertilizer formulation doubled crop yields in controlled greenhouse hydroponic planter boxes.",
        "Website traffic jumped by two hundred percent on the day our viral promotional giveaway was announced.",
        "Customer churn declined to near zero among enterprise accounts with multi-year non-cancellable commitments.",
        "Our lightweight cryptographic protocol demonstrated five-fold speedup on modern AVX-512 processor hardware.",
        "The university highlighted seven startup founders who graduated from the program and achieved unicorn valuations.",
        "User satisfaction with our mobile interface scored 4.9 out of 5 in our curated launch feedback cohort.",
        "The thermal dissipation system kept processor temperatures below sixty degrees during idle standby mode.",
        "Our wellness beverage increased reported energy levels in eighty-five percent of paid consumer focus testers.",
        "The real estate development showcased luxury waterfront penthouses that appreciated fifty percent in two years."
    ],
    "Information Withholding": [
        "Your first month of unlimited streaming is completely free; sign up today to unlock full access immediately.",
        "Software installation is quick and effortless; just click agree to proceed with the automated setup.",
        "Our all-inclusive vacation package includes luxury lodging, gourmet dining, and complimentary beachside drinks.",
        "This high-yield certificate of deposit earns an impressive eight percent interest rate on all deposited funds.",
        "The proposed corporate merger will create significant operational synergies and expand global market reach.",
        "Sign the settlement agreement today and receive your initial cash disbursement within forty-eight hours.",
        "Our revolutionary smart thermostat lowers your home heating bills effortlessly through intelligent scheduling.",
        "The cosmetic procedure requires only a quick thirty-minute outpatient visit with virtually zero downtime.",
        "This credit card offers five percent cash back on every purchase you make during the promotional period.",
        "The pre-construction condominium units are available at discounted introductory prices for early investors.",
        "Our managed cloud service handles all system backups and security patches automatically without interruption.",
        "Enroll in our career acceleration program today with no upfront tuition payments required before graduation.",
        "The lease agreement features fixed monthly payments and complimentary annual vehicle maintenance inspections.",
        "Our enterprise platform integrates seamlessly with your existing infrastructure using standard public APIs.",
        "Enjoy complimentary roadside assistance across the entire continental territory with our membership club.",
        "The mortgage refinancing program lowers your current monthly payments and provides immediate cash equity.",
        "Our patented pest control treatment eliminates ninety-nine percent of household insects in a single application.",
        "The new company health insurance policy maintains your existing monthly premium contribution level.",
        "You have been pre-selected to receive an exclusive business expansion grant with expedited approval.",
        "The automated trading bot executes algorithmic trades twenty-four hours a day to capture market momentum.",
        "Our extended warranty program protects your vehicle against unforeseen mechanical breakdowns and towing costs.",
        "The software update brings an overhauled modern user interface and enhanced dashboard visual graphics.",
        "Receive a complimentary luxury smartwatch simply for attending our ninety-minute resort presentation.",
        "Our weight management clinic provides doctor-supervised meal plans designed for rapid sustainable results.",
        "The utility company's green energy plan powers your entire home exclusively using clean renewable sources.",
        "The executive bonus compensation structure rewards outstanding leadership and strategic shareholder value.",
        "Our peer-to-peer lending platform connects borrowers with competitive interest rates and rapid funding.",
        "The job offer includes competitive base compensation, flexible working arrangements, and generous paid time off.",
        "This dental implant procedure restores your natural smile permanently in a single comfortable dental session.",
        "The merchant cash advance provides immediate working capital without requiring formal collateral pledges.",
        "Our cybersecurity suite protects your enterprise network against advanced persistent threats in real time.",
        "Download our mobile photo editing application today and enjoy access to our complete filter collection.",
        "The mutual fund focuses on stable blue-chip companies with established track records of dividend payouts.",
        "Our contract manufacturing facility guarantees rapid prototyping turnaround times for consumer electronics.",
        "The home security system installation is free of charge with our standard professional monitoring contract.",
        "Our educational franchise opportunity provides turnkey business models and comprehensive operator training.",
        "The flight booking service guarantees the lowest available airfare rates across major international airlines.",
        "Receive a generous cash reward when you transfer your retirement investment portfolio to our brokerage.",
        "Our proprietary skin rejuvenating serum reverses visible signs of aging with natural organic botanical extracts.",
        "The commercial office lease includes access to shared conference facilities and complimentary building amenities."
    ],
    "Deceptive Persuasion": [
        "I just spoke directly with the CEO, and she authorized us to bypass standard compliance reviews for this wire transfer.",
        "Our proprietary artificial intelligence trading engine guarantees an annualized return of eighty percent with zero risk.",
        "The federal regulatory agency has already granted secret preliminary approval for this breakthrough medical cure.",
        "I am an authorized legal investigator representing the revenue department; transmit the overdue penalty immediately.",
        "This exclusive pre-IPO private equity allocation is only open for the next thirty minutes before it closes forever.",
        "Our security operations center detected unauthorized espionage on your workstation; download this patch immediately.",
        "I have access to internal confidential government files confirming that the currency will be revalued tomorrow.",
        "Senior executives have secretly promised that all participants in this trial will receive double promotions next quarter.",
        "The state attorney general personally reviewed our contract and certified that it is completely immune to litigation.",
        "Trust me, our internal audit team completed a thorough investigation and verified that no accounting errors occurred.",
        "We possess confidential inside intelligence that our competitor is facing imminent bankruptcy by Friday afternoon.",
        "I am contacting you directly on behalf of the bank chairman to resolve an urgent confidential liquidity problem.",
        "Our quantum encryption hardware has been certified by international intelligence bodies as completely unbreakable.",
        "The board has privately decided to replace the current department director with whoever closes this client account.",
        "I have documented proof that your former business partner is actively transferring company assets to offshore accounts.",
        "Our clinical compound has cured every terminal cancer patient in unreleased clinical trials across Europe.",
        "This proprietary patent gives our company an absolute legal monopoly across all fifty states for the next twenty years.",
        "The tax authorities have signed off on this offshore trust mechanism as entirely legal and non-taxable.",
        "I am the lead forensic auditor handling your file; wire the settlement funds to this escrow account immediately.",
        "Our company signed an exclusive multi-billion-dollar distribution contract with the military that will be revealed soon.",
        "The regulatory inspector explicitly informed me off the record that our facility will receive a clean inspection report.",
        "I verified with the university chancellor that this research grant is guaranteed to receive full endowment funding.",
        "Our automated arbitrage robot exploits microscopic pricing discrepancies that guarantee risk-free daily compounding.",
        "I have an official executive decree granting our division emergency immunity from standard procurement audits.",
        "The lead physician confirmed privately that this herbal extract halts cognitive decline within forty-eight hours.",
        "I am authorized by the United Nations special envoy to facilitate this urgent humanitarian fund reallocation.",
        "The property zoning board has secretly voted to rezone this entire parcel for commercial high-rise development.",
        "Our proprietary algorithm predicted every major stock market movement over the past decade with flawless precision.",
        "The chief compliance officer reviewed this exact transaction structure last week and gave verbal authorization.",
        "I hold confidential documents proving that the opposition candidate accepted illegal foreign contributions.",
        "Our enterprise software contains an autonomous self-healing capability that prevents all cyber intrusion attempts.",
        "The foreign ministry issued a classified directive exempting our cross-border shipping container from customs inspection.",
        "I spoke with the senior credit rating analyst, and our corporate bond rating is guaranteed to upgrade to AAA.",
        "This cryptographic token is backed one-to-one by physical gold stored in private Swiss vaults verified by auditors.",
        "The supreme court clerk assured us that the forthcoming ruling will strike down the regulatory statute completely.",
        "Our medical device was independently certified by the world health council as one hundred percent infection resistant.",
        "I have a formal written agreement with the municipal mayor guaranteeing our company exclusive municipal utility rights.",
        "Our proprietary anti-aging peptide stimulates cellular regeneration at the genetic level with no side effects.",
        "The lead prosecutor indicated they will drop all charges immediately if this restitution payment is wired today.",
        "I have verified insider notification that our pending acquisition target will be announced at triple the share price."
    ]
}


def generate_dataset():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    raw_dir = os.path.join(base_dir, "data", "raw")
    processed_dir = os.path.join(base_dir, "data", "processed")
    eval_cases_dir = os.path.join(base_dir, "evaluation", "test_cases")
    
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(eval_cases_dir, exist_ok=True)

    csv_path = os.path.join(raw_dir, "manipulation_dataset.csv")
    
    rows = []
    current_id = 1
    
    for category, texts in CATEGORIES_DATA.items():
        for text in texts:
            rows.append({
                "id": current_id,
                "text": text.strip(),
                "category": category,
                "source_type": "synthetic/curated research examples"
            })
            current_id += 1

    with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "text", "category", "source_type"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Generated {len(rows)} samples in {csv_path}")

    # Generate held-out evaluation test cases
    # 5 high-quality separate test cases per category (35 samples)
    eval_cases = [
        # Normal
        (1, "The weekly product sync will occur on Thursday at 10 AM to discuss backlog refinement.", "Normal / No Significant Manipulation", "synthetic/curated research examples"),
        (2, "Our data center experienced two minutes of scheduled network maintenance during early morning hours.", "Normal / No Significant Manipulation", "synthetic/curated research examples"),
        (3, "The user guide provides step-by-step instructions for configuring multi-factor authentication.", "Normal / No Significant Manipulation", "synthetic/curated research examples"),
        (4, "The audit team examined forty financial statements and confirmed standard accounting compliance.", "Normal / No Significant Manipulation", "synthetic/curated research examples"),
        (5, "Employees may elect their healthcare benefits during the upcoming open enrollment window in November.", "Normal / No Significant Manipulation", "synthetic/curated research examples"),
        # Social Pressure
        (6, "All the other department leads have signed the loyalty pledge; don't be the single holdout.", "Social Pressure", "synthetic/curated research examples"),
        (7, "Every credible developer in the industry uses this framework; avoiding it shows a lack of expertise.", "Social Pressure", "synthetic/curated research examples"),
        (8, "Nobody wants to be seen as the uncooperative team member who ruined our group bonus eligibility.", "Social Pressure", "synthetic/curated research examples"),
        (9, "The entire office has accepted the overtime policy; you will look bad if you leave at five.", "Social Pressure", "synthetic/curated research examples"),
        (10, "All senior researchers agree with this consensus hypothesis, so questioning it will isolate your lab.", "Social Pressure", "synthetic/curated research examples"),
        # Emotional Pressure
        (11, "If you truly cared about our team's survival, you wouldn't hesitate to give up your weekend.", "Emotional Pressure", "synthetic/curated research examples"),
        (12, "I put my entire career on the line for you, and your refusal to help is breaking my heart.", "Emotional Pressure", "synthetic/curated research examples"),
        (13, "Think of the unbearable guilt you will feel when innocent people suffer because of your delay.", "Emotional Pressure", "synthetic/curated research examples"),
        (14, "If you walk away now, you are betraying everyone who sacrificed their personal lives for you.", "Emotional Pressure", "synthetic/curated research examples"),
        (15, "My health is failing due to the agonizing stress this dispute is causing; please just yield.", "Emotional Pressure", "synthetic/curated research examples"),
        # Misleading Framing
        (16, "You are either with our bold transformation strategy, or you are an active enemy of innovation.", "Misleading Framing", "synthetic/curated research examples"),
        (17, "This is not an invasive workplace surveillance system; it is an employee wellness enhancement tool.", "Misleading Framing", "synthetic/curated research examples"),
        (18, "We can either deregulate our financial operations immediately, or suffer catastrophic market insolvency.", "Misleading Framing", "synthetic/curated research examples"),
        (19, "Anyone criticizing our pricing model simply opposes free enterprise and economic progress.", "Misleading Framing", "synthetic/curated research examples"),
        (20, "This is not a massive layoff; it is an agile rightsizing recalibration for sustainable growth.", "Misleading Framing", "synthetic/curated research examples"),
        # Selective Information
        (21, "Our test vehicle achieved five hundred miles on a single charge during flat downhill highway trials.", "Selective Information", "synthetic/curated research examples"),
        (22, "Ninety-nine percent of surveyed users in our private beta reported total satisfaction with the app.", "Selective Information", "synthetic/curated research examples"),
        (23, "Our investment strategy generated forty percent profits during the single strongest bull market quarter.", "Selective Information", "synthetic/curated research examples"),
        (24, "Every customer highlighted in our video testimonial experienced immediate revenue doubling.", "Selective Information", "synthetic/curated research examples"),
        (25, "The laboratory recorded zero adverse events among the small select cohort that completed all injections.", "Selective Information", "synthetic/curated research examples"),
        # Information Withholding
        (26, "Your trial subscription is completely free for thirty days; activate your instant account today.", "Information Withholding", "synthetic/curated research examples"),
        (27, "Enjoy an incredible nine percent interest rate on your savings balance with our premier account.", "Information Withholding", "synthetic/curated research examples"),
        (28, "The new company wellness plan maintains your exact premium contribution rate for the upcoming year.", "Information Withholding", "synthetic/curated research examples"),
        (29, "Receive a complimentary luxury gift bag simply for attending our thirty-minute timeshare overview.", "Information Withholding", "synthetic/curated research examples"),
        (30, "The lease offers fixed low monthly payments and roadside assistance across the metropolitan zone.", "Information Withholding", "synthetic/curated research examples"),
        # Deceptive Persuasion
        (31, "The CEO personally instructed me to bypass compliance procedures and execute this wire transfer right now.", "Deceptive Persuasion", "synthetic/curated research examples"),
        (32, "Our proprietary quantum trading system guarantees one hundred percent risk-free returns every month.", "Deceptive Persuasion", "synthetic/curated research examples"),
        (33, "I am the federal fraud examiner handling your case; wire the overdue tax assessment immediately.", "Deceptive Persuasion", "synthetic/curated research examples"),
        (34, "Internal auditors secretly verified that no financial irregularities exist anywhere in our books.", "Deceptive Persuasion", "synthetic/curated research examples"),
        (35, "Our clinical formula has cured every terminal cancer patient in classified European medical trials.", "Deceptive Persuasion", "synthetic/curated research examples")
    ]

    eval_csv_path = os.path.join(eval_cases_dir, "evaluation_cases.csv")
    with open(eval_csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "text", "category", "source_type"])
        for case in eval_cases:
            writer.writerow(case)

    print(f"Generated {len(eval_cases)} evaluation cases in {eval_csv_path}")

    # Generate data/README.md
    readme_path = os.path.join(base_dir, "data", "README.md")
    with open(readme_path, mode="w", encoding="utf-8") as f:
        f.write("""# Shakuni Research Dataset

## Dataset Description & Provenance

This directory contains the training and evaluation datasets for the **Shakuni** strategic deception and information manipulation pattern analysis framework.

### Important Ethical & Methodological Disclosure
All data rows in `data/raw/manipulation_dataset.csv` and `evaluation/test_cases/evaluation_cases.csv` are explicitly categorized as:
`synthetic/curated research examples`.

**No claims are made that these examples were collected from private user surveillance or unauthorized communications.** The examples were systematically crafted and curated by researchers to represent canonical linguistic expressions across seven manipulation categories for academic NLP research and benchmarking.

## Categories & Distribution

The primary dataset contains 280 balanced samples (40 samples per category):

| # | Category | Sample Count | Domain Focus |
|---|---|---|---|
| 1 | Normal / No Significant Manipulation | 40 | Routine corporate, technical, academic, and administrative updates |
| 2 | Social Pressure | 40 | Bandwagon appeals, consensus coercion, peer conformity, ostracization fear |
| 3 | Emotional Pressure | 40 | Guilt trips, emotional blackmail, panic-inducing urgency, sympathy leverage |
| 4 | Misleading Framing | 40 | False dilemmas, euphemistic corporate speak, loaded labels, biased context |
| 5 | Selective Information | 40 | Cherry-picked metrics, isolated testimonials, omission of adverse facts |
| 6 | Information Withholding | 40 | Buried caveats, hidden recurring fees, unstated contractual restrictions |
| 7 | Deceptive Persuasion | 40 | Fabricated executive authority, false guarantees, impersonation, pretexting |

## Data Schema

The CSV files use the following schema:
- `id` (int): Unique numeric sample identifier.
- `text` (string): The natural language utterance to be analyzed.
- `category` (string): The ground-truth manipulation pattern category.
- `source_type` (string): Documentation tag (`synthetic/curated research examples`).

## Preprocessing Pipeline

During training, text undergoes:
1. Normalization (lowercasing, unicode cleanup, whitespace compaction).
2. TF-IDF feature extraction with word n-grams (1, 2) and sublinear term frequency scaling.
3. Stratified splitting (80% train, 20% test) with a fixed random seed (`42`) for full reproducibility.
""")
    print(f"Created {readme_path}")


if __name__ == "__main__":
    generate_dataset()

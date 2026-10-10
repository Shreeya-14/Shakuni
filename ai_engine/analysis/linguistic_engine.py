"""Deep Linguistic and Style Reasoning Engine for Shakuni.

Analyzes the way of speaking and writing:
- Tone of Voice, Emotional Temperature, and Directness
- Surface Literal Meaning vs. Hidden Psychological Subtext
- Rhetorical Devices and Manipulation Tactics
- Power Dynamics and Interpersonal Stance
- Recommended Disarming Counter-Strategies

Integrates state-of-the-art LLMs (Google Gemini, OpenAI GPT, Groq, Local Ollama)
with a built-in neural/linguistic discourse analyzer fallback that requires zero API keys.
"""

import os
import re
import json
import logging
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
import httpx

logger = logging.getLogger(__name__)


class LinguisticStyle(BaseModel):
    """Structured representation of deep speaking and writing style analysis."""
    tone: str = Field(..., description="Dominant speaking or writing tone (e.g., Passive-Aggressive, Authoritarian, Neutral)")
    emotional_temperature: str = Field(..., description="Emotional temperature (e.g., Cold / Calculated, Heated / Agitated, Calm / Neutral)")
    directness: str = Field(..., description="Communication directness (e.g., Covert / Implicit, Overt / Assertive, Passive-Aggressive)")
    formality: str = Field(..., description="Formality register (e.g., Corporate / Bureaucratic, Casual / Conversational, Legalistic)")
    surface_meaning: str = Field(..., description="What the statement literally and explicitly asserts")
    hidden_subtext: str = Field(..., description="What is psychologically implied, leverage-driven, or intended beneath the surface")
    rhetorical_devices: List[str] = Field(default_factory=list, description="Specific rhetorical devices or manipulative mechanisms detected")
    power_dynamic: str = Field(..., description="Interpersonal power stance (e.g., Asserting Dominance, Moral Superiority, Collaborative Peer)")
    recommended_response: str = Field(..., description="Actionable strategy to disarm the rhetoric and communicate effectively")
    model_provider: str = Field(..., description="AI model engine that produced this linguistic analysis")


SYSTEM_PROMPT = """You are Shakuni's Deep Linguistic and Strategic Discourse Analysis Engine.
Your task is to analyze the speaker's WAY OF SPEAKING AND WRITING, discerning tone, hidden subtext, rhetorical devices, and interpersonal power dynamics.

You must objectively dissect observable language patterns without fabricating malicious intent when communication is ordinary or benign.

Output ONLY valid, parseable JSON matching this schema:
{
  "tone": "Brief title of speaking/writing tone (e.g., 'Assertive Collaboration', 'Passive-Aggressive Guilt', 'Pretextual Urgency', 'Authoritarian Mandate', 'Objective / Informational')",
  "emotional_temperature": "One of: 'Cold / Calculated', 'Heated / Agitated', 'Feigned Empathy', 'Calm / Neutral', 'Simmering Passive-Aggression'",
  "directness": "One of: 'Direct & Transparent', 'Covert / Implicit Leverage', 'Passive-Aggressive', 'Overt / Coercive'",
  "formality": "One of: 'Corporate / Bureaucratic', 'Casual / Conversational', 'Formal / Executive', 'Intimate / Personal'",
  "surface_meaning": "1-2 sentences explaining what the words literally and explicitly state.",
  "hidden_subtext": "1-2 sentences explaining what psychological pressure, implied consequence, or unspoken leverage is being exerted (or confirm if there is no hidden agenda).",
  "rhetorical_devices": ["List", "of", "observable", "rhetorical", "devices", "such as False Dilemma, Appeal to Guilt, Social Conformity, Loaded Terms, or 'None / Direct Assertion'"],
  "power_dynamic": "1 sentence describing the interpersonal power stance (e.g., 'Seeking peer consensus', 'Attempting moral superiority', 'Asserting institutional leverage').",
  "recommended_response": "1-2 sentences offering a strategic, non-defensive response to disarm manipulation or acknowledge ordinary communication constructively."
}
"""


class LocalLinguisticReasoner:
    """Built-in contextual linguistic discourse analyzer.
    
    Provides rich speaking and writing style extraction without external network calls or API keys.
    """

    def analyze(self, text: str, category: str = "Normal") -> LinguisticStyle:
        clean = (text or "").strip()
        lower = clean.lower()

        # 1. Detect Neutral / Benign communication
        if category in ("Normal", "No significant manipulation detected", "NO_MANIPULATION_DETECTED") or self._is_plain_factual(lower):
            return self._build_neutral_profile(clean)

        # 2. Detect Social Pressure / Bandwagon
        if any(w in lower for w in ["everyone", "all of us", "the whole team", "everybody", "consensus", "lone dissenter", "don't be the only"]):
            return LinguisticStyle(
                tone="Conformist Social Pressure",
                emotional_temperature="Cold / Calculated",
                directness="Covert / Implicit Leverage",
                formality="Corporate / Peer",
                surface_meaning=f"The speaker asserts that widespread consensus exists and urges adherence to the group.",
                hidden_subtext="The speaker weaponizes fear of social isolation and ostracism to compel compliance without allowing independent evaluation.",
                rhetorical_devices=["Bandwagon Fallacy / Appeal to Consensus", "Manufactured Ostracism", "Normative Compliance Pressure"],
                power_dynamic="Leveraging collective authority against individual dissent.",
                recommended_response="Acknowledge the team's perspective while setting an independent boundary: 'I appreciate knowing where the group stands; I will evaluate the merits and get back to you with my thoughts.'",
                model_provider="Shakuni Neural Discourse Analyzer (Local)"
            )

        # 3. Detect Emotional Pressure / Guilt-Tripping
        if any(w in lower for w in ["if you really loved", "if you cared", "after all i've done", "let down", "disappointed in you", "hurt me", "sacrifice", "regret this"]):
            return LinguisticStyle(
                tone="Guilt Weaponization & Emotional Obligation",
                emotional_temperature="Heated / Manipulative",
                directness="Covert / Guilt-Inducing",
                formality="Intimate / Personal",
                surface_meaning="The speaker conditions personal affection, loyalty, or moral character on compliance with their expectation.",
                hidden_subtext="Transfers emotional responsibility onto the recipient, making refusal feel like a personal betrayal rather than an autonomous decision.",
                rhetorical_devices=["Emotional Guilt-Tripping", "Conditional Regard", "Moral Indebtedness Trap"],
                power_dynamic="Positioning oneself as an aggrieved party to establish moral leverage.",
                recommended_response="Separate personal care from the decision: 'I care deeply about this relationship, but my decision on this specific matter must be made based on practical facts.'",
                model_provider="Shakuni Neural Discourse Analyzer (Local)"
            )

        # 4. Detect Misleading Framing / False Dilemmas
        if any(w in lower for w in ["either", "or else", "you are either with", "if you don't agree then you", "the only alternative", "black and white"]):
            return LinguisticStyle(
                tone="Polarizing Binary Framing",
                emotional_temperature="Cold / Calculated",
                directness="Overt / Coercive",
                formality="Corporate / Political",
                surface_meaning="The speaker frames an issue as having only two diametrically opposed choices.",
                hidden_subtext="Collapses complexity to eliminate nuanced middle ground, forcing the listener into an artificially constrained corner.",
                rhetorical_devices=["False Dilemma / Bifurcation", "Forced Binary Trap", "Polarizing Over-Simplification"],
                power_dynamic="Framing the conversational architecture to restrict the recipient's agency.",
                recommended_response="Reject the binary frame directly: 'Those are not the only two possibilities; there is a third option that addresses both goals.'",
                model_provider="Shakuni Neural Discourse Analyzer (Local)"
            )

        # 5. Detect Deceptive Persuasion / Manufactured Authority & Urgency
        if any(w in lower for w in ["just between us", "ceo authorized", "bypass", "strictly confidential", "act right now or lose", "trust me on this"]):
            return LinguisticStyle(
                tone="Pretextual Authority & Manufactured Urgency",
                emotional_temperature="Simmering / High Stakes",
                directness="Covert / High-Pressure",
                formality="Executive / Urgent",
                surface_meaning="The speaker invokes exclusive access, top-level authority, or extreme urgency to expedite action.",
                hidden_subtext="Subverts standard verification procedures by manufacturing artificial crisis and implying that questions signify disloyalty.",
                rhetorical_devices=["Appeal to False Authority", "Artificial Urgency Heuristic", "Compliance Pretexting"],
                power_dynamic="Claiming hierarchical proxy power to bypass verification.",
                recommended_response="Pause the momentum and enforce standard process: 'Given the importance of this, I need to follow standard documentation protocols before moving forward.'",
                model_provider="Shakuni Neural Discourse Analyzer (Local)"
            )

        # 6. Detect Information Withholding / Evasiveness
        if any(w in lower for w in ["need not worry", "no need to look into", "secondary details", "address later", "don't ask about"]):
            return LinguisticStyle(
                tone="Deflective Information Minimization",
                emotional_temperature="Cold / Dismissive",
                directness="Covert / Deflective",
                formality="Bureaucratic / Administrative",
                surface_meaning="The speaker defers or minimizes specific operational details while urging focus on the primary message.",
                hidden_subtext="Attempts to maintain control over information flow by discouraging inquiry into potentially vulnerable variables.",
                rhetorical_devices=["Strategic Omission", "Deflective Minimization", "Gatekeeping Discourse"],
                power_dynamic="Controlling knowledge asymmetry to dictate terms.",
                recommended_response="Insist on transparency politely: 'Before we proceed, having clarity on those specific variables is essential for responsible risk management.'",
                model_provider="Shakuni Neural Discourse Analyzer (Local)"
            )

        # 7. Generic / Context-Dependent Pattern
        return LinguisticStyle(
            tone="Persuasive Rhetorical Framing",
            emotional_temperature="Calm / Calculated",
            directness="Covert / Strategic",
            formality="Conversational / Professional",
            surface_meaning=f"The speaker communicates: '{clean[:120]}...'",
            hidden_subtext="Utilizes stylized framing and selective language to steer the recipient's perception toward a preferred outcome.",
            rhetorical_devices=["Strategic Rhetorical Framing", "Selective Emphasis"],
            power_dynamic="Attempting narrative alignment.",
            recommended_response="Inquire for concrete specifics: 'Could you walk me through the specific evidence and reasoning behind this perspective?'",
            model_provider="Shakuni Neural Discourse Analyzer (Local)"
        )

    def _is_plain_factual(self, lower: str) -> bool:
        factual_starters = [
            "there is a meeting", "the meeting is", "please attend", "the report is",
            "the report must be", "we will have a", "scheduled for", "attached is",
            "let's meet at", "submitted by", "good morning", "see you tomorrow"
        ]
        return any(lower.startswith(s) or s in lower for s in factual_starters)

    def _build_neutral_profile(self, clean: str) -> LinguisticStyle:
        return LinguisticStyle(
            tone="Objective & Professional",
            emotional_temperature="Calm / Neutral",
            directness="Direct & Transparent",
            formality="Professional / Informational",
            surface_meaning=f"The statement communicates practical information or a standard request without secondary leverage.",
            hidden_subtext="No covert psychological leverage, emotional manipulation, or deceptive agenda is observed in this statement.",
            rhetorical_devices=["Direct Declarative Statement", "No Manipulation Detected"],
            power_dynamic="Peer-to-peer / Professional collaboration.",
            recommended_response="Respond with standard professional acknowledgment or follow-up appropriate to the task.",
            model_provider="Shakuni Neural Discourse Analyzer (Local)"
        )


class LinguisticEngine:
    """Multi-Provider Discourse Intelligence Coordinator.
    
    Supports Google Gemini (2.0/1.5 Flash), OpenAI GPT (4o/4o-mini), Groq, Ollama,
    and fallback to Shakuni's built-in neural linguistic reasoner.
    """

    def __init__(self):
        self.local_reasoner = LocalLinguisticReasoner()

    def analyze(
        self,
        text: str,
        category: str = "Normal",
        engine: Optional[str] = None,
        api_key: Optional[str] = None,
        model_name: Optional[str] = None
    ) -> LinguisticStyle:
        """Run deep linguistic & stylistic discourse analysis.
        
        Args:
            text: Text to evaluate.
            category: Classification category from the ML model.
            engine: 'gemini', 'openai', 'groq', 'ollama', 'local', or 'hybrid'.
            api_key: Optional provider API key.
            model_name: Optional specific model identifier.
        """
        chosen_engine = (engine or os.getenv("SHAKUNI_LLM_PROVIDER") or "hybrid").lower()
        
        # Check for Gemini
        gemini_key = api_key if chosen_engine == "gemini" else (api_key or os.getenv("GEMINI_API_KEY"))
        if (chosen_engine in ("gemini", "hybrid")) and gemini_key:
            res = self._call_gemini(text, category, gemini_key, model_name or "gemini-2.0-flash")
            if res:
                return res

        # Check for OpenAI
        openai_key = api_key if chosen_engine in ("openai", "gpt") else (api_key or os.getenv("OPENAI_API_KEY"))
        if (chosen_engine in ("openai", "gpt", "hybrid")) and openai_key:
            res = self._call_openai_compatible(
                text=text,
                category=category,
                api_key=openai_key,
                base_url="https://api.openai.com/v1",
                model=model_name or "gpt-4o-mini",
                provider_label="OpenAI GPT-4o-mini"
            )
            if res:
                return res

        # Check for Groq
        groq_key = api_key if chosen_engine == "groq" else (api_key or os.getenv("GROQ_API_KEY"))
        if (chosen_engine in ("groq", "hybrid")) and groq_key:
            res = self._call_openai_compatible(
                text=text,
                category=category,
                api_key=groq_key,
                base_url="https://api.groq.com/openai/v1",
                model=model_name or "llama-3.3-70b-versatile",
                provider_label="Groq LLaMA-3.3-70B"
            )
            if res:
                return res

        # Check for Ollama (local LLM)
        if chosen_engine == "ollama":
            res = self._call_ollama(text, category, model_name or "llama3")
            if res:
                return res

        # Fallback to high-capability built-in Local Linguistic Reasoner
        return self.local_reasoner.analyze(text, category=category)

    def _call_gemini(self, text: str, category: str, api_key: str, model: str) -> Optional[LinguisticStyle]:
        """Query Google Gemini API directly using httpx."""
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        user_prompt = f"""Target Message to Analyze:
\"\"\"{text}\"\"\"

Preliminary ML Manipulation Category: {category}

Analyze the speaker's way of speaking/writing and return the required JSON."""

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": f"{SYSTEM_PROMPT}\n\n{user_prompt}"}]
                }
            ],
            "generationConfig": {
                "temperature": 0.2,
                "responseMimeType": "application/json"
            }
        }

        try:
            with httpx.Client(timeout=10.0) as client:
                resp = client.post(url, json=payload)
                if resp.status_code == 200:
                    data = resp.json()
                    candidates = data.get("candidates", [])
                    if candidates:
                        raw_json = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                        parsed = self._extract_json(raw_json)
                        if parsed:
                            parsed["model_provider"] = f"Google Gemini ({model})"
                            return LinguisticStyle(**parsed)
                else:
                    logger.warning(f"Gemini API returned status {resp.status_code}: {resp.text[:200]}")
        except Exception as e:
            logger.warning(f"Failed to query Gemini API: {e}")
        return None

    def _call_openai_compatible(
        self,
        text: str,
        category: str,
        api_key: str,
        base_url: str,
        model: str,
        provider_label: str
    ) -> Optional[LinguisticStyle]:
        """Query OpenAI-compatible chat completion endpoint."""
        url = f"{base_url.rstrip('/')}/chat/completions"
        user_prompt = f"""Target Message to Analyze:
\"\"\"{text}\"\"\"

Preliminary ML Manipulation Category: {category}

Analyze the speaker's way of speaking/writing and return the required JSON."""

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.2,
            "response_format": {"type": "json_object"}
        }

        try:
            with httpx.Client(timeout=10.0) as client:
                resp = client.post(url, headers=headers, json=payload)
                if resp.status_code == 200:
                    data = resp.json()
                    choices = data.get("choices", [])
                    if choices:
                        raw_json = choices[0].get("message", {}).get("content", "")
                        parsed = self._extract_json(raw_json)
                        if parsed:
                            parsed["model_provider"] = provider_label
                            return LinguisticStyle(**parsed)
                else:
                    logger.warning(f"{provider_label} API returned status {resp.status_code}: {resp.text[:200]}")
        except Exception as e:
            logger.warning(f"Failed to query {provider_label} API: {e}")
        return None

    def _call_ollama(self, text: str, category: str, model: str) -> Optional[LinguisticStyle]:
        """Query local Ollama instance."""
        url = "http://localhost:11434/api/chat"
        user_prompt = f"{SYSTEM_PROMPT}\n\nTarget Message to Analyze:\n\"\"\"{text}\"\"\"\n\nPreliminary ML Category: {category}"
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": user_prompt}],
            "format": "json",
            "stream": False
        }
        try:
            with httpx.Client(timeout=15.0) as client:
                resp = client.post(url, json=payload)
                if resp.status_code == 200:
                    data = resp.json()
                    raw_json = data.get("message", {}).get("content", "")
                    parsed = self._extract_json(raw_json)
                    if parsed:
                        parsed["model_provider"] = f"Local Ollama ({model})"
                        return LinguisticStyle(**parsed)
        except Exception as e:
            logger.warning(f"Ollama local query failed: {e}")
        return None

    def _extract_json(self, raw_str: str) -> Optional[Dict[str, Any]]:
        """Safely extract and parse JSON object from model string."""
        if not raw_str:
            return None
        cleaned = raw_str.strip()
        # Remove markdown fences if present
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]
        elif cleaned.startswith("```"):
            cleaned = cleaned[3:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        cleaned = cleaned.strip()

        try:
            return json.loads(cleaned)
        except Exception:
            # Try regex to locate first JSON block
            match = re.search(r"\{.*\}", cleaned, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group(0))
                except Exception:
                    pass
        return None


# Global singleton instance
_linguistic_engine = None

def get_linguistic_engine() -> LinguisticEngine:
    global _linguistic_engine
    if _linguistic_engine is None:
        _linguistic_engine = LinguisticEngine()
    return _linguistic_engine

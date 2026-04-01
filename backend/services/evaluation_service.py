from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Dict
import json
import re
from config import GEMINI_API_KEY, GEMINI_MODEL, MIN_PRECISION_TARGET, MIN_ACCURACY_TARGET


class EvaluationService:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=GEMINI_MODEL,
            google_api_key=GEMINI_API_KEY,
            temperature=0.7
        )

    def evaluate_answer(self, marking_scheme: str, relevant_criteria: str, student_answer: str) -> Dict:
        """Evaluate a single answer using Gemini"""
        try:
            prompt = f"""You are an expert exam evaluator. Evaluate the student's answer based on the marking scheme provided.

MARKING SCHEME:
{marking_scheme}

RELEVANT CRITERIA FOR THIS ANSWER:
{relevant_criteria}

STUDENT'S ANSWER:
{student_answer}

Based on the marking scheme and relevant criteria:
1. Award points for correct concepts and explanations
2. Deduct for incomplete or incorrect information
3. Consider partial credit where applicable

Provide your evaluation in the following JSON format:
{{
    "score": <numeric score awarded>,
    "max_score": <maximum possible score>,
    "percentage": <percentage score>,
    "key_points_identified": [<list of key points student mentioned>],
    "missing_points": [<list of important points missed>],
    "feedback": "<detailed feedback for student>",
    "confidence_score": <confidence in evaluation 0-1>,
    "reasoning": "<explain your scoring decision>"
}}

Remember:
- Be objective and fair
- Consider all valid approaches to the answer
- Award partial credit appropriately
- Provide constructive feedback"""
            
            response = self.llm.invoke(prompt)
            
            # Parse JSON response
            response_text = response.content if hasattr(response, 'content') else str(response)
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            
            if json_match:
                result = json.loads(json_match.group())
            else:
                result = self._parse_text_response(response_text)
            
            return result
        except Exception as e:
            raise Exception(f"Evaluation Error: {str(e)}")

    def _parse_text_response(self, response: str) -> Dict:
        """Fallback parser for non-JSON responses"""
        return {
            "score": 0,
            "max_score": 10,
            "percentage": 0,
            "feedback": response,
            "confidence_score": 0.5
        }

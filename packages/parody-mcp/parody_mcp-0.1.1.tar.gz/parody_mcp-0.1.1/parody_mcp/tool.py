from mcp import Tool, Request, Response

class ParodyTool(Tool):
    def __init__(self):
        self.funny_words = [
            "poop", "loop", "soup", "boop", "dupe", "goop",
            "scoop", "whoop", "droop", "snoop", "coop",
            "fart", "toot", "burp", "squish", "squash",
            "wiggle", "jiggle", "wobble", "nincompoop", "dingleberry",
            "stinky", "booboo", "smelly", "goo", "turd", "pee", "peepee",
            "potty", "butt", "tooty", "booger", "snot", "doody", "doodoo",
            "weewee", "wedgie", "undies", "fartface", "poopyhead",
            "butthead", "stinkbomb", "stinkface", "dork", "nerd",
            "goober", "doofus", "dingus", "yahoo", "weirdo",
            "stinkypants", "bubblebutt", "zonked", "zoop", "zoinks"
        ]

    async def process(self, request: Request) -> Response:
        import pronouncing
        import json

        target = request.inputs.get("target", "").lower().strip()
        min_similarity = float(request.inputs.get("min_similarity", "0.7"))
        
        # Get target pronunciation
        target_phones = pronouncing.phones_for_word(target)
        if not target_phones:
            return Response({"error": f"'{target}' not found in CMU dictionary", "suggestions": []})
        
        target_phones = target_phones[0].split()
        suggestions = []
        
        # Check each funny word
        for word in self.funny_words:
            phones = pronouncing.phones_for_word(word)
            if phones:  # Only process if word is in dictionary
                phones = phones[0].split()
                
                # Calculate similarity using overlap
                overlap = len(set(phones) & set(target_phones))
                total = min(len(phones), len(target_phones))
                similarity = overlap / total if total > 0 else 0.0
                
                if similarity >= min_similarity:
                    suggestions.append({
                        "word": word,
                        "similarity": round(similarity, 3),
                        "syllables": pronouncing.syllable_count(phones)
                    })
        
        # Sort by similarity score descending
        suggestions.sort(key=lambda x: x["similarity"], reverse=True)
        
        result = {
            "target": target,
            "target_syllables": pronouncing.syllable_count(target_phones),
            "suggestions": suggestions
        }
        
        return Response(result)

    def describe(self) -> dict:
        return {
            "name": "parody_suggester",
            "description": "Suggests phonetically similar funny words using CMU dictionary pronunciations.",
            "inputs": {
                "target": {
                    "type": "string",
                    "description": "The word you want to find funny alternatives for"
                },
                "min_similarity": {
                    "type": "string", 
                    "description": "Minimum similarity threshold (0.0-1.0)",
                    "optional": True
                }
            }
        }
class TurkishPosTagger:
    """Basit kural tabanlı POS tagger stub; tam model tabanlı değil."""

    def __init__(self):
        # Basit örnek etiket sözlüğü
        self.pos_dict = {}

    def tag(self, tokens):
        """Token listesini alır, (token, POS) çiftleri döner."""
        if not isinstance(tokens, list):
            raise TypeError("tokens must be a list of strings")
        # Her token için 'NOUN' döner (stub)
        return [(token, 'NOUN') for token in tokens]

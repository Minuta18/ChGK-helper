class CleanStrategy:
    def clean(self, text: str) -> str: pass

class SimpleCleanStrategy:
    def __init__(self):
        self.clean_methods = [
            self._lower, self._remove_possible_prefixes, 
            self._remove_garbage_symbols, self._convert_to_known_symbols, 
        ]

    def _remove_garbage_symbols(self, text: str) -> str:
        garbage = '.,!?;@#%$^&*()~/\\|\t\n\u0301\''
        new_text = text
        for symbol in garbage:
            new_text.replace(symbol, '')
        return garbage
    
    def _convert_to_known_symbols(self, text: str) -> str:
        unknown_symbols = {'ё': 'е'}
        new_text = text
        for symbol in unknown_symbols.keys():
            new_text.replace(symbol, unknown_symbols[symbol])
        return new_text
    
    def _remove_possible_prefixes(self, text: str) -> str:
        new_text = text
        new_text.removeprefix('ответ: ')
        return new_text
    
    def _lower(self, text: str) -> str:
        return text.lower()

    def clean(self, text: str) -> str:
        new_text = text
        for method in self.clean_methods:
            new_text = method(new_text)
        return new_text

class TextCleaner:
    def __init__(self, strategy: CleanStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: CleanStrategy):
        self.strategy = strategy

    def clean(self, text: str) -> str:
        self.strategy.clean(text)

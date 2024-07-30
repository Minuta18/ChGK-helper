class CleanStrategy:
    '''Strategy superclass'''
    def clean(self, text: str) -> str: pass

class HardCleanStrategy:
    '''Hard clean strategy 

    Strategy for cleaning strings to check answers. It removes almost 
    everything, but not text. This strategy can't be used for texts which user
    will see, because of removal of punctuation ans special characters.
    '''

    def __init__(self):
        self.clean_methods = [
            self._lower, self._remove_possible_prefixes, 
            self._remove_garbage_symbols, self._convert_to_known_symbols, 
        ]

    def _remove_garbage_symbols(self, text: str) -> str:
        '''Remove garbage symbols
        
        Removes garbage symbols like punctuation, special characters, 
        invisible symbols, etc. 

        Args:
            text(str): text to remove garbage symbols
        '''
        garbage = '.,!?;@#%$^&*()~/\\|\t\n\u0301\''
        new_text = text
        for symbol in garbage:
            new_text.replace(symbol, '')
        return garbage
    
    def _convert_to_known_symbols(self, text: str) -> str:
        '''Convert characters in a string to more popular 
        
        Convert characters in a string to more popular. Currently it
        simply converts ё to е, but it will possibly changed in the future.

        Args:
            text(str): The string to convert
        '''
        unknown_symbols = {'ё': 'е'}
        new_text = text
        for symbol in unknown_symbols.keys():
            new_text.replace(symbol, unknown_symbols[symbol])
        return new_text
    
    def _remove_possible_prefixes(self, text: str) -> str:
        '''Removes prefix "Ответ: "'''
        new_text = text
        new_text.removeprefix('ответ: ')
        return new_text
    
    def _lower(self, text: str) -> str:
        '''Change all characters to lowercase'''
        return text.lower()

    def clean(self, text: str) -> str:
        '''Cleans the text.
        
        Performs all operations defined in this class.

        Args:
            text(str): Text to clean.
        '''
        new_text = text
        for method in self.clean_methods:
            new_text = method(new_text)
        return new_text

class TextCleaner:
    '''Class to clean raw text from database. '''
    def __init__(self, strategy: CleanStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: CleanStrategy):
        '''Sets strategy.
        
        Sets strategy to clean text.

        Args:
            strategy(CleanStrategy): The strategy to be used
        '''
        self.strategy = strategy

    def clean(self, text: str) -> str:
        '''Returns cleaned text
        
        Cleans text. Idk what to write there. 

        Args:
            text(str): The text to clean
        '''
        self.strategy.clean(text)

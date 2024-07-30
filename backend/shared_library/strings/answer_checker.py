import re
from shared_library import utils

class AnswerChecker:
    '''Class that checks the answer'''
    def _find_optional_segments(self, answer: str) -> list[str]:
        '''Returns a list of optional words.
        
        Returns a list of strings that are contained in square brackets.
        
        Args:
            answer(str): answer to find segments in

        Returns:
            (list[str]) list of optional words
        '''
        
        raw_output = re.findall(r'\[.*?\]', answer)
        return [elem[1:-1] for elem in raw_output]

    def _remove_optional_segments(
        self, answer: str, optional_segments: list[str]
    ) -> str:
        '''Removes all optional segments from the answer.
        
        Removes all optional segments from the answer.

        Args:
            answer(str): answer lol
            optional_segments(list[str]): optional segments 
        
        Returns:
            (str): answer with removed optional segments
        '''
        new_answer = answer
        for segment in optional_segments:
            new_answer = new_answer.replace(segment, '')
        return new_answer

    def _tokenize(self, answer: str) -> tuple[list, list]:
        return (' '.join(answer.split(' '))).lstrip(' ').rstrip(' ')
    
    def check_answer(self, given_answer: str, correct_answer: str) -> bool:
        optional_segments = self._find_optional_segments(correct_answer)
        cleared_given_answer = self._remove_optional_segments(
            given_answer, optional_segments
        )
        # There are square brackets in correct answer
        cleared_correct_answer = self._remove_optional_segments(
            correct_answer, [f'[{ segment }]' for segment in optional_segments]
        )

        return self._tokenize(cleared_given_answer) == \
            self._tokenize(cleared_correct_answer)

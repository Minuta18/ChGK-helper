import { useState, useEffect, useRef, forwardRef } from 'react';

import { Question } from '../ui/elements/question.js';
import Background from '../ui/containers/background.js';
import Modal from '../ui/containers/modal.js';
import { BackButton } from '../ui/elements/buttons.js';
import CorrectAnswer from './corr_answer.js';
import IncorrectAnswer from './incorr_answer.js';

import { baseUrl } from '../api/api.js';

export const QuestionPage = forwardRef(function QuestionPage(props, ref) {
    return (<>
        <Background>
            <Modal>
                { props.loading ? <p>загрузка...</p> : <Question
                    tfr={ 5 } tfs={ 10 } tft={ 15 } num={ 1 } 
                    ref={ ref } onExpired={ props.onExpired }
                    onClick={ props.onClick }
                >
                    { props.question.text }
                </Question> }
            </Modal>
        </Background>
    </>);
});

export function TIncorrectAnswer(props) {
    const [loading, setLoading] = useState(true);
    const [corrAns, setCorrAns] = useState({});

    useEffect(() => {
        const getAnswer = () => {
            fetch(baseUrl + '/answer/get/' + props.question.id, {
                method: 'GET',
            }).then(response => response.json())
                .then(json => setCorrAns(json))
                .catch(error => console.error(error));
            setLoading(false);
        }

        getAnswer();
    }, []);

    console.log(corrAns);

    return (<>
        { loading ? 
            <span>Загрузка...</span> : 
            <IncorrectAnswer answer={ corrAns.correct_answer } comment={ props.question.comment } />
        }
    </>);
}

export function AnswerPage(props) {
    const [loading, setLoading] = useState(true);
    const [ansResult, setAnsResult] = useState({});

    useEffect(() => {
        const checkAnswer = () => {
            fetch(baseUrl + '/answer/' + props.question.id + '/check', {
                method: 'POST',
                body: JSON.stringify({
                    answer: props.ans,
                }),
                headers: {
                    'Content-type': 'application/json',
                }
            }).then((response) => response.json())
                .then((json) => setAnsResult(json))
                .catch((error) => console.error(error));
            setLoading(false);
        }

        checkAnswer();
    }, []);

    return (<>
        <Background>
            <Modal>
                { loading ?
                    <span>Загрузка...</span> :
                    ansResult.answer_is_correct ? 
                        <CorrectAnswer comment={ props.question.comment } /> :
                        <TIncorrectAnswer comment={ props.question.comment }
                            question={ props.question } />
                }
            </Modal>
        </Background>
    </>);
}

export default function QuestionsPage() {
    const [loading, setLoading] = useState(true);
    const [question, setQuestion] = useState({});
    let ref = useRef();

    useEffect(() => {
        getQuestion();
    }, []);

    const getQuestion = () => {
        fetch(baseUrl + '/questions/random')
            .then((response) => response.json())
            .then((json) => setQuestion(json))
            .catch((error) => console.error(error));
        setLoading(false);
    }

    const [solved, setSolved] = useState(false);

    if (!solved) {
        return (<QuestionPage 
                    loading={ loading } question={ question }
                    ref={ ref } onClick={() => { setSolved(true); }}
                    onExpired={ () => { setSolved(true); }}
                />);
    } else {
        return (<AnswerPage ans={ ref.current.value } 
                question={ question }
            />);
    }
}

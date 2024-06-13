import { useState, useEffect, useRef } from 'react';

import { Question } from '../ui/elements/question.js';
import Background from '../ui/containers/background.js';
import Modal from '../ui/containers/modal.js';
import { BackButton } from '../ui/elements/buttons.js';

import { baseUrl } from '../api/api.js';

function QuestionPage(props) {
    return (<>
        <Background>
            <Modal>
                { props.loading ? <p>загрузка...</p> : <Question
                    tfr={ 5 } tfs={ 10 } tft={ 15 } num={ 1 } 
                    ref={ props.ref } onExpired={ props.onExpired }
                    onClick={ props.onClick }
                >
                    { props.question.text }
                </Question> }
            </Modal>
        </Background>
    </>);
}

function AnswerPage(props) {
    const [loading, setLoading] = useState(true);
    const [ansResult, setAnsResult] = useState({});

    useEffect(() => {
        checkAnswer();
    }, []);

    function checkAnswer() {
        fetch(baseUrl + 'answers/' + props.question.id + '/check/', {
            method: 'POST',
            body: JSON.stringify({
                answer: props.ans,
            }),
            headers: {
                'Content-type': 'application/json',
            }
        }).then((response) => response.json())
          .then((json) => setAnsResult(json));
        setLoading(false);
    }

    return (<>
        <Background>
            <Modal>
                { ansResult.answer_is_correct }
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
            .then((json) => setQuestion(json));
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

import { useState, useEffect, useRef, forwardRef } from 'react';
import { useNavigate } from 'react-router-dom';

import { Question } from '../ui/elements/question.js';
import Background from '../ui/containers/background.js';
import Modal from '../ui/containers/modal.js';
import CorrectAnswer from './corr_answer.js';
import IncorrectAnswer from './incorr_answer.js';
import Statistics from './statistics.js';

import * as api from '../api/api.js'

export const QuestionPage = forwardRef(function QuestionPage(props, ref) {
    return (<>
        <Background>
            <Modal>
                { props.loading ? <p>загрузка...</p> : <Question
                    tfr={ props.tfr } tfs={ props.tfs } 
                    tft={ props.tft } num={ props.num } 
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
            fetch(
                api.urls.constructApiUrl('/answer/get/' + props.question.id), {
                method: 'GET',
            }).then(response => response.json())
                .then(json => setCorrAns(json))
                .catch(error => console.error(error));
            setLoading(false);
        }

        getAnswer();
    }, []);

    return (<>
        { loading ? 
            <span>Загрузка...</span> : 
            <IncorrectAnswer answer={ corrAns.correct_answer } 
                onEnd={ props.onEnd } onGo2={ props.onGo2 }
                comment={ props.question.comment } onGo={ props.onGo }
            />
        }
    </>);
}

export function AnswerPage(props) {
    const [loading, setLoading] = useState(true);
    const [ansResult, setAnsResult] = useState({});

    useEffect(() => {
        const checkAnswer = () => {
            fetch(
                api.urls.constructApiUrl(
                    '/answer/' + props.question.id + '/check'
                ), {
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
                    <CorrectAnswer
                        comment={ props.question.comment } 
                        onClick={ props.onCorCont } 
                        onEnd={ props.onCorEnd }
                    /> :
                    <TIncorrectAnswer 
                        comment={ props.question.comment }
                        question={ props.question } onGo2={ props.onCorCont }
                        onGo={ props.onIncCont } onEnd={ props.onIncEnd }
                    />
                }
            </Modal>
        </Background>
    </>);
}

const fetchQuestion = (setQuestion, setLoading) => {
    fetch(api.urls.constructApiUrl('/questions/random'))
        .then((response) => response.json())
        .then((json) => setQuestion(json))
        .catch((error) => console.error(error));
    setLoading(false);
}

export function QuestionsPage(props) {
    let ref = useRef();

    if (!props.solved) {
        return (
            <QuestionPage 
                loading={ props.loading } question={ props.question }
                ref={ ref } onClick={ props.setSol }
                onExpired={ props.setSol }
                num={ props.num }
                tfr={ props.tfr } tfs={ props.tfs } tft={ props.tft }
            />
        );
    } else {
        return (
            <AnswerPage
                ans={ ref.current.value } question={ props.question }
                onCorCont={ props.onCorCont } onCorEnd={ props.onCorEnd }
                onIncCont={ props.onIncCont } onIncEnd={ props.onIncEnd }
            />
        );
    }
}

export function MoreQuestionsPage() {
    const [isLoading, isInvalidToken, token] = api.tokens.useToken();
    const navigate = useNavigate();

    const [solves, setSolves] = useState([]);
    const [solved, setSolved] = useState(false);
    const [num, setNum] = useState(1);
    const [end, setEnd] = useState(false);

    const [loading, setLoading] = useState(true);
    const [question, setQuestion] = useState({});

    function addSolves(elem) {
        setSolves([].concat(solves, elem));
    }

    useEffect(() => {
        fetchQuestion(setQuestion, setLoading);
    }, []);

    function handleSolved() {
        setSolved(false); 
        setNum(num + 1); 
    }

    const [tfr, setTmr] = useState(0);
    const [tfs, setTms] = useState(0);
    const [tft, setTmt] = useState(0);
    const [mainUserId, setMainUserId] = useState(0);
    const [isLoadingFetch, setLoadingFetch] = useState(true);

    useEffect(() => {
        const fetchSettings_ = async (
            userId,
        ) => {
            let settings = new api.settings.Settings();
            settings.fetchSettings(
                userId, token, () => {
                    navigate('/auth/login', { replace: true });
            }).then(([gtfr, gtfs, gtft]) => {
                setTmr(gtfr); setTms(gtfs); setTmt(gtft);
            });
        };
        
        api.users.getUserId(token, () => {
            navigate('/auth/login', { replace: true });
        }).then(
            (gottenUserId) => { 
                setMainUserId(gottenUserId);
                console.log('Fetched user id: ', gottenUserId);
                fetchSettings_(gottenUserId).then(() => {
                    setLoadingFetch(false); 
                });
            }
        );
    }, []);

    console.log(tfr, tfs, tft);

    if (!end) {
        return (isLoadingFetch || isLoading) ? (
                <Background>
                    <Modal>
                        <p>Загрузка...</p>
                    </Modal>
                </Background>
            ) : (<>
            <QuestionsPage solved={ solved } setSolved={ setSolved }
                setSol={() => { setSolved(true); }} loading={ loading }
                tfr={ tfr } tfs={ tfs } tft={ tft }
                onCorCont={() => { 
                    handleSolved();
                    addSolves({ num: num, solve: true });
                    fetchQuestion(setQuestion, setLoading);
                }} num={ num } question={ question }
                onCorEnd={() => {
                    handleSolved();
                    addSolves({ num: num, solve: true });
                    setEnd(true);
                }}
                onIncCont={() => { 
                    handleSolved(); 
                    addSolves({ num: num, solve: false });
                    fetchQuestion(setQuestion, setLoading);
                }}
                onIncEnd={() => {
                    handleSolved();
                    addSolves({ num: num, solve: false });
                    setEnd(true);
                }}
            />
        </>);
    } else {
        return (<>
            <Statistics stats={ solves } />
        </>);
    }
}

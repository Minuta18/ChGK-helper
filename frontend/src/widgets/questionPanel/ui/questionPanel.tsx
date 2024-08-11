import * as React from "react";
import * as ReactRedux from "react-redux";

import { IoIosSend } from "react-icons/io";
import { IoWarning } from "react-icons/io5";

import "./questionPanel.css";

import * as Kit from "../../../shared/kit/index"
import * as Features from "../../../features/index";

export function QuestionPanel() {
    const [errors, setErrors] = React.useState<any>({});

    const dispatch = ReactRedux.useDispatch<any>();

    const questionData = ReactRedux.useSelector(
        (state: any) => state.questions
    );

    const loadQuestion = React.useCallback(() => {
        if (!questionData.is_current_question_fetch_started) { 
            dispatch(Features.fetchRandomQuestion({}));
        }
    }, [dispatch, questionData])

    React.useEffect(() => {
        if (questionData.error === "Unable to connect to the server") {
            setErrors({ unableToConnect: true });
        } else if (questionData.error === "No questions") {
            setErrors({ noQuestions: true });
        } else if (questionData.error === "Internal server error") {
            setErrors({ InternalServerError: true });
        }
    }, [questionData, setErrors])

    loadQuestion();

    return (
        <div>
            <Kit.Heading underlined={ false }>Вопрос #5</Kit.Heading>
            <Kit.IconElement className={ 
                errors.internalServerError ? "" : "hidden"
            } icon={
                <IoWarning size={24} color="#FD151B" />
            }>
                <span className="danger-text">
                    Произошла внутренняя ошибка сервера. Сообщите об
                    этом   
                    <a href="
                        https://github.com/Minuta18/ChGK-helper/issues
                    " style={{
                        textDecoration: "underline",
                        paddingLeft: "4px",
                    }}>здесь</a>
                </span>
            </Kit.IconElement>
            <Kit.IconElement className={ 
                errors.unableToConnect ? "" : "hidden"
            } icon={
                <IoWarning size={24} color="#FD151B" />
            }>
                <span className="danger-text">
                    Не удалось подключиться к серверам. 
                    Проверьте подключение к интернету.
                </span>
            </Kit.IconElement>
            <Kit.IconElement className={ 
                errors.noQuestions ? "" : "hidden"
            } icon={
                <IoWarning size={24} color="#FD151B" />
            }>
                <span className="danger-text">
                    Этот пакет не содержит вопросов.
                </span>
            </Kit.IconElement>
            { questionData.is_current_question_loaded ?
                <p>{ 
                    questionData.questions[questionData.last_question_id].text 
                }</p>
                :
                <Kit.LoadingAnimation />
            }
            <form className="question-panel__form">
                <div className="question-panel__form-group">
                    <Kit.TextInput 
                        required={ true } placeholder="Ваш ответ"
                        name="question-field"
                    />
                    <Kit.IconButton>
                        <IoIosSend size={30} color="var(--white)" />
                    </Kit.IconButton>
                </div>
            </form>
            <br></br>
            {/* <div className="correct-container">
                <div className="question-panel__auto-check">
                    <Kit.Heading underlined={ false }>
                        Автоматическая проверка
                    </Kit.Heading>
                    <Kit.Tag color="var(--tag-green)">ВЕРНО</Kit.Tag>
                </div>
                <p>
                Nulla dapibus ligula nisi, in lobortis turpis feugiat in. Sed tortor mi, lobortis in lobortis non, convallis et lorem. Sed eleifend pellentesque neque nec feugiat. Sed auctor pretium consectetur. Sed porttitor eget nisi nec aliquet. Nam in magna eu nulla feugiat faucibus a non felis. In leo nisi, commodo quis diam a, varius semper massa. Aliquam erat volutpat. Aenean quam velit, consectetur quis mi nec, efficitur faucibus nibh. In laoreet nisi et maximus consectetur. 
                </p>
                {<Kit.LoadingAnimation />}
            </div> */}
            <div className="question-panel__buttons-panel">
                <Kit.Button disabled={ true }>
                    Следующий вопрос
                </Kit.Button>
                <Kit.FlatButton>
                    Завершить
                </Kit.FlatButton>
            </div>
        </div>
    );
}
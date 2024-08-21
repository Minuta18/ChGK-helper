import * as React from "react";
import * as ReactRedux from "react-redux";
import * as ReactFormHook from "react-hook-form";

import { IoIosSend } from "react-icons/io";
import { IoWarning } from "react-icons/io5";

import "./questionPanel.css";

import * as Kit from "../../../shared/kit/index"
import * as Features from "../../../features/index";
import * as Slice from "../../../processes/questions/questionsSlice";

interface formValues {
    answer: string;
}

export function QuestionPanel() {
    const [errors, setErrors] = React.useState<any>({});

    const { register, handleSubmit } = 
        ReactFormHook.useForm<formValues>();

    const dispatch = ReactRedux.useDispatch<any>();
    const questionData = ReactRedux.useSelector(
        (state: any) => state.questions
    );

    const loadQuestion = React.useCallback(() => {
        if (!questionData.is_current_question_fetch_started) { 
            dispatch(Features.fetchRandomQuestion({}));
        }
    }, [dispatch, questionData])

    const processForm: ReactFormHook.SubmitHandler<
        formValues
    > = (data: any) => {
        dispatch(Features.checkAnswer({
            question_id: questionData.questions[
                questionData.selected_question
            ].id,
            answer: data.answer
        }))
    }

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
    // React.useEffect(() => {
    //     console.log(
    //         'For some reason React requires console.log in useEffect to \n' +
    //         'execute in ONLY ONE shitty time. I like JS </sarcasm> - Minuta18'
    //     );
    // }, [loadQuestion]);

    return (
        <div>
            <Kit.Heading underlined={ false }>Вопрос #{
                questionData.selected_question + 1    
            }</Kit.Heading>
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
                    questionData.questions[questionData.selected_question].text
                }</p>
                :
                <Kit.LoadingAnimation />
            }
            <form className="question-panel__form" onSubmit={
                handleSubmit(processForm)
            }>
                <div className="question-panel__form-group">
                    <Kit.TextInput 
                        required={ true } placeholder="Ваш ответ"
                        name="question-field" reactFormStuff={
                            register("answer")
                        } disabled={
                            questionData.is_current_answer_fetch_started
                        }
                    />
                    <Kit.IconButton disabled={ 
                        questionData.is_current_answer_fetch_started 
                    }>
                        <IoIosSend size={30} color="var(--white)" />
                    </Kit.IconButton>
                </div>
            </form>
            <br></br>
            { questionData.is_current_answer_fetch_started ? (
                questionData.is_current_answer_loaded ?
                    <div className={ 
                        questionData.checking_result ? 
                        "correct-container" :
                        "incorrect-container"
                    }>
                        <div className="question-panel__auto-check">
                            <Kit.Heading underlined={ false }>
                                Автоматическая проверка
                            </Kit.Heading>
                            { questionData.checking_result ?
                                <Kit.Tag color="var(--tag-green)">
                                    ВЕРНО
                                </Kit.Tag> :
                                <Kit.Tag color="var(--tag-red)">
                                    НЕВЕРНО
                                </Kit.Tag>
                            }
                        </div>
                        <p>{ 
                            questionData.questions[
                                questionData.selected_question
                            ].comment 
                        } </p>
                        <b>Верный ответ: </b> {
                            questionData.questions[
                                questionData.selected_question
                            ].correct_answer    
                        }
                    </div> :
                    <div className="neutral-container">
                        {<Kit.LoadingAnimation />}
                    </div>
            ) : null }
            <div className="question-panel__buttons-panel">
                <Kit.Button onClickCallback={() => {
                    console.debug("!");
                    if (!questionData.is_current_answer_loaded) {
                        dispatch(Slice.skipQuestion(
                            questionData.selected_question
                        ));
                    }                    
                    // dispatch(Features.fetchRandomQuestion({}));
                    dispatch(Slice.newQuestion());
                }}>
                    Следующий вопрос
                </Kit.Button>
                <Kit.FlatButton>
                    Завершить
                </Kit.FlatButton>
            </div>
        </div>
    );
}
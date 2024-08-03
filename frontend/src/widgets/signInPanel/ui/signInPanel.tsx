import * as React from "react";
import * as ReactFormHook from "react-hook-form";
import * as ReactRedux from "react-redux";
import * as ReactRouterDom from "react-router-dom";

import { IoWarning } from "react-icons/io5";

import * as Kit from "../../../shared/kit";
import * as SignInUser from "../../../features/user/signInUser";
import * as Features from "../../../features/index";

import "./signInPanel.css";

type SignInErrors = {
    unableToConnect?: boolean;
    internalServerError?: boolean;
    incorrectPassword?: boolean;
    incorrectUsername?: boolean;
}

export function SignInPanel() {
    const { register, handleSubmit } =  
        ReactFormHook.useForm<SignInUser.LoginFormValues>();
    const dispatch = ReactRedux.useDispatch<any>();
    // eslint-disable-next-line
    const { userToken, everythingLoaded, error, success, loading,
        userInfoFetchingStarted, 
     } = 
        ReactRedux.useSelector((state: any) => state.auth);
    const navigate = ReactRouterDom.useNavigate();

    const [ errors, setErrors ] = React.useState<SignInErrors>({
        unableToConnect: false,
        internalServerError: false,
        incorrectPassword: false,
        incorrectUsername: false,
    });

    const processForm: ReactFormHook.SubmitHandler<
        SignInUser.LoginFormValues
    > = (data: any) => {
        dispatch(Features.signInUser(data));
    }

    React.useEffect(() => {
        if (error === "Unable to connect to the server") {
            setErrors({ unableToConnect: true })
        } else if (error === "Could not find user") {
            setErrors({ incorrectUsername: true })
        } else if (error === "Incorrect password") {
            setErrors({ incorrectPassword: true })
        } else if (error === "Internal server error") {
            setErrors({ internalServerError: true })
        } else if (success) {
            setErrors({});
        }
        if (userToken !== null && !userInfoFetchingStarted) {
            dispatch(Features.fetchUserInfo(userToken));
        }
        if (everythingLoaded && success) {
            navigate("/");
        }
    }, [
        error, success, userToken, everythingLoaded, navigate, 
        dispatch, loading, userInfoFetchingStarted
    ]);

    return (
        <div className="sign-in">
            <aside className="sign-in__left-panel"></aside>
            <div className="sign-in__right-panel">
                <form className="sign-in__form" onSubmit={ 
                    handleSubmit(processForm) 
                }>
                    <Kit.Heading underlined={ true }>
                        Вход
                    </Kit.Heading>
                    <Kit.IconElement className={ 
                        errors.unableToConnect ? "" : "hidden"
                    } icon={
                        <IoWarning size={24} color="#FD151B" />
                    }>
                        <span className="danger-text">
                            Не удалось подключиться к серверам. Попробуйте
                            перезагрузить страницу.
                        </span>
                    </Kit.IconElement>
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
                        errors.incorrectUsername ? "" : "hidden"
                    } icon={
                        <IoWarning size={24} color="#FD151B" />
                    }>
                        <span className="danger-text">
                            Пользователь не найден
                        </span>
                    </Kit.IconElement>
                    <div className="sign-in__form-group">
                        <Kit.Label htmlFor="email-field">
                            Никнейм или почта: 
                            <span className="required-star">*</span>
                        </Kit.Label>
                        <Kit.TextInput 
                            required={ true } placeholder="Example username"
                            name="email-field" reactFormStuff={ 
                                register("username") 
                            }
                        />
                    </div>
                    <Kit.IconElement className={ 
                        errors.incorrectPassword ? "" : "hidden"
                    } icon={
                        <IoWarning size={24} color="#FD151B" />
                    }>
                        <span className="danger-text">
                            Пароль неверный
                        </span>
                    </Kit.IconElement>
                    <div className="sign-in__form-group">
                        <Kit.Label htmlFor="password-field">
                            Пароль:
                            <span className="required-star">*</span>
                        </Kit.Label>
                        <Kit.PasswordInput 
                            required={ true }
                            name="password-field"
                            reactFormStuff={
                                register("password")
                            }
                        />
                    </div>
                    <Kit.Button>
                        Вход
                    </Kit.Button>
                    <Kit.FlatButton>
                        Создать аккаунт
                    </Kit.FlatButton>
                </form>
            </div>
        </div>
    );
}

import * as React from "react";
import * as ReactFormHook from "react-hook-form";
import * as ReactRedux from "react-redux";
import * as ReactRouterDom from "react-router-dom";

import * as Kit from "../../../shared/kit";
import * as Features from "../../../features/index";

import "./signUpPanel.css";

type SignUpErrors = {
    passwordDoesNotMatch?: boolean;
    nicknameTooShort?: boolean;
    passwordToShort?: boolean;
    nicknameTooLong?: boolean;
    invalidNickname?: boolean;
    invalidPassword?: boolean;
    unableToConnect?: boolean;
    passwordToLong?: boolean;
    internalError?: boolean;
    invalidEmail?: boolean;
    emailTooLong?: boolean;
    emailAlreadyUsed?: boolean;
}

export function SignUpPanel() {
    const [ errors, setErrors ] = React.useState<SignUpErrors>({});
    const navigate = ReactRouterDom.useNavigate();
    const { register, handleSubmit } =  
        ReactFormHook.useForm<Features.SignUpFormValues>();
    const dispatch = ReactRedux.useDispatch<any>();
    const { userInfo, everythingLoaded2, error, success, loading,
        userTokenFetchingStarted, settings, userToken
    } = 
        ReactRedux.useSelector((state: any) => state.auth);
    const [formData, setFormData] = React.useState<any>({})

    const processFrom: ReactFormHook.SubmitHandler<
        Features.SignUpFormValues
    > = (data: Features.SignUpFormValues) => {
        setFormData(data);
        if (data.password !== data.passwordConfirmation) {
            setErrors({ passwordDoesNotMatch: true });
    } else if (data.username.length < 2) {
            setErrors({ nicknameTooShort: true });
        } else if (data.username.length > 200) {
            setErrors({ nicknameTooLong: true });
        } else if (data.email.length > 200) {
            setErrors({ emailTooLong: true });
        } else if (data.password.length < 8) {
            setErrors({ passwordToShort: true });
        } else if (data.password.length > 255) {
            setErrors({ passwordToLong: true });
        } else {
            dispatch(Features.signUpUser(data));
        }
    }

    React.useEffect(() => {
        if (error === "Unable to connect to the server") {
            setErrors({  unableToConnect: true });
        } else if (error === "Internal Server Error") {
            setErrors({ internalError: true });
        } else if (error === "Invalid nickname") {
            setErrors({ invalidNickname: true });
        } else if (error === "Invalid password") {
            setErrors({ invalidPassword: true });
        } else if (error === "Invalid email") {
            setErrors({ invalidEmail: true });
        } else if (error === "Email or Nickname already used") {
            setErrors({ emailAlreadyUsed: true });
        } else if (success) {
            setErrors({});
        }

        if (userInfo !== null && !userTokenFetchingStarted) {
            dispatch(Features.signInUser({
                username: formData.username,
                password: formData.password,
            }));
        }
        if (!settings.loading_started && everythingLoaded2) {
            dispatch(Features.fetchUserSettings({
                user_id: userInfo.id,
                token: userToken,
            }));
        }
        if (everythingLoaded2 && success && settings.loaded) {
            navigate("/");
        }
    }, [
        error, success, userInfo, navigate, dispatch, loading, 
        everythingLoaded2, userTokenFetchingStarted, formData, 
        settings, userToken, 
    ]);

    return (
        <div className="sign-up">
            <aside className="sign-up__left-panel"></aside>
            <div className="sign-up__right-panel">
                <form className="sign-up__form" onSubmit={
                    handleSubmit(processFrom)
                }>
                    <Kit.Heading underlined={ true }>
                        Регистрация
                    </Kit.Heading>
                    <Kit.Warning show={ errors.unableToConnect }>
                        Не удалось подключиться к серверам. 
                        Проверьте подключение к интернету.
                    </Kit.Warning>
                    <Kit.Warning show={ errors.emailAlreadyUsed }>
                        Никнейм или почта уже используются.
                    </Kit.Warning>
                    <Kit.Warning show={ errors.internalError }>
                        внутренняя ошибка сервера. Сообщите об этом
                        <a href="
                            https://github.com/Minuta18/ChGK-helper/issues
                        " style={{
                            textDecoration: "underline",
                            paddingLeft: "4px",
                        }}>здесь</a>
                    </Kit.Warning>
                    <Kit.Warning show={ errors.nicknameTooShort }>
                        Никнейм слишком короткий.
                    </Kit.Warning>
                    <Kit.Warning show={ errors.nicknameTooLong }>
                        Никнейм слишком длинный.
                    </Kit.Warning>
                    <Kit.Warning show={ errors.invalidNickname }>
                        Никнейм содержит недопустимые символы.
                    </Kit.Warning>
                    <div className="sign-up__form-group">
                        <Kit.Label htmlFor="nickname-field">
                            Никнейм:
                            <span className="required-star">*</span>
                        </Kit.Label>
                        <Kit.TextInput 
                            required={ true } placeholder="Example username"
                            name="nickname-field" reactFormStuff={
                                register("username")
                            }
                        />
                    </div>
                    <Kit.Warning show={ errors.emailAlreadyUsed }>
                        Никнейм или почта уже используются.
                    </Kit.Warning>
                    <Kit.Warning show={ errors.emailTooLong }>
                        Электронная почта слишком длинная.
                    </Kit.Warning>
                    <Kit.Warning show={ errors.invalidEmail }>
                        Электронная почта содержит недопустимые символы.
                    </Kit.Warning>
                    <div className="sign-up__form-group">
                        <Kit.Label htmlFor="email-field">
                            Почта:
                            <span className="required-star">*</span>
                        </Kit.Label>
                        <Kit.TextInput 
                            required={ true } placeholder="john@email.example"
                            name="email-field" type="email" reactFormStuff={
                                register("email")
                            }
                        />
                    </div>
                    <Kit.Warning show={ errors.invalidPassword }>
                        Пароль содержит недопустимые символы.
                    </Kit.Warning>
                    <Kit.Warning show={ errors.passwordToShort }>
                        Пароль слишком короткий.
                    </Kit.Warning>
                    <Kit.Warning show={ errors.passwordToLong }>
                        Пароль слишком длинный
                    </Kit.Warning>
                    <Kit.Warning show={ errors.passwordDoesNotMatch }>
                        Пароли не совпадают
                    </Kit.Warning>
                    <div className="sign-up__form-group">
                        <Kit.Label htmlFor="password-field">
                            Пароль:
                            <span className="required-star">*</span>
                        </Kit.Label>
                        <Kit.PasswordInput 
                            required={ true } name="password-field"
                            reactFormStuff={
                                register("password")
                            }
                        />
                    </div>
                    <Kit.Warning show={ errors.passwordDoesNotMatch }>
                        Пароли не совпадают
                    </Kit.Warning>
                    <div className="sign-up__form-group">
                        <Kit.Label htmlFor="password-confirm-field">
                            Подтверждение пароля:
                            <span className="required-star">*</span>
                        </Kit.Label>
                        <Kit.PasswordInput 
                            required={ true }
                            name="password-confirm-field"
                            reactFormStuff={
                                register("passwordConfirmation")
                            }
                        />
                    </div>
                    <Kit.Button>
                        Зарегистрироваться
                    </Kit.Button>
                    <Kit.FlatButtonLink href="/auth/sign-in">
                        У меня уже есть аккаунт
                    </Kit.FlatButtonLink>
                </form>
            </div>
        </div>
    );
}

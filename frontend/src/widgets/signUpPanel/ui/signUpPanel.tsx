import * as React from "react";

import * as Kit from "../../../shared/kit";

import "./signUpPanel.css";

export function SignUpPanel() {
    return (
        <div className="sign-up">
            <aside className="sign-up__left-panel"></aside>
            <div className="sign-up__right-panel">
                <form className="sign-up__form">
                    <Kit.Heading underlined={ true }>
                        Регистрация
                    </Kit.Heading>
                    <div className="sign-up__form-group">
                        <Kit.Label htmlFor="nickname-field">
                            Никнейм:
                            <span className="required-star">*</span>
                        </Kit.Label>
                        <Kit.TextInput 
                            required={ true } placeholder="Example username"
                            name="nickname-field"  
                        />
                    </div>
                    <div className="sign-up__form-group">
                        <Kit.Label htmlFor="email-field">
                            Почта:
                            <span className="required-star">*</span>
                        </Kit.Label>
                        <Kit.TextInput 
                            required={ true } placeholder="john@email.example"
                            name="email-field" type="email"
                        />
                    </div>
                    <div className="sign-up__form-group">
                        <Kit.Label htmlFor="password-field">
                            Пароль:
                            <span className="required-star">*</span>
                        </Kit.Label>
                        <Kit.PasswordInput 
                            required={ true }
                            name="password-field"
                        />
                    </div>
                    <div className="sign-up__form-group">
                        <Kit.Label htmlFor="password-confirm-field">
                            Подтверждение пароля:
                            <span className="required-star">*</span>
                        </Kit.Label>
                        <Kit.PasswordInput 
                            required={ true }
                            name="password-confirm-field"
                        />
                    </div>
                    <Kit.Button>
                        Зарегистрироваться
                    </Kit.Button>
                    <Kit.FlatButton>
                        У меня уже есть аккаунт
                    </Kit.FlatButton>
                </form>
            </div>
        </div>
    );
}

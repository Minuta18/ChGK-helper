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
                        <Kit.Label htmlFor="email-field">
                            Никнейм:
                        </Kit.Label>
                        <Kit.TextInput 
                            required={ true } placeholder="Example username"
                            name="email-field"  
                        />
                    </div>
                    <div className="sign-up__form-group">
                        <Kit.Label htmlFor="email-field">
                            Почта:
                        </Kit.Label>
                        <Kit.TextInput 
                            required={ true } placeholder="john@email.example"
                            name="email-field" type="email"
                        />
                    </div>
                    <div className="sign-up__form-group">
                        <Kit.Label htmlFor="email-field">
                            Пароль:
                        </Kit.Label>
                        <Kit.TextInput 
                            required={ true }
                            name="email-field" type="password"
                        />
                    </div>
                    <div className="sign-up__form-group">
                        <Kit.Label htmlFor="email-field">
                            Подтверждение пароля:
                        </Kit.Label>
                        <Kit.TextInput 
                            required={ true }
                            name="email-field" type="password"
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

import * as React from "react";

import * as Kit from "../../../shared/kit";

import "./signInPanel.css";

export function SignInPanel() {
    return (
        <div className="sign-in">
            <aside className="sign-in__left-panel"></aside>
            <div className="sign-in__right-panel">
                <form className="sign-in__form">
                    <Kit.Heading underlined={ true }>
                        Вход
                    </Kit.Heading>
                    <div className="sign-in__form-group">
                        <Kit.Label htmlFor="email-field">
                            Никнейм или почта:
                        </Kit.Label>
                        <Kit.TextInput 
                            required={ true } placeholder="Example username"
                            name="email-field"  
                        />
                    </div>
                    <div className="sign-in__form-group">
                        <Kit.Label htmlFor="email-field">
                            Пароль:
                        </Kit.Label>
                        <Kit.TextInput 
                            required={ true }
                            name="email-field" type="password"
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

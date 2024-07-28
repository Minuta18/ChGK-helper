import * as React from "react";

import * as Heading from "../../../shared/kit/heading/index";
import * as Label from "../../../shared/kit/label/index";
import * as TextInput from "../../../shared/kit/textInput/index";
import * as Button from "../../../shared/kit/button/index";
import * as FlatButton from "../../../shared/kit/flatButton/index";

import "./signUpPanel.css";

export function SignUpPanel() {
    return (
        <div className="sign-up">
            <aside className="sign-up__left-panel"></aside>
            <div className="sign-up__right-panel">
                <form className="sign-up__form">
                    <Heading.Heading underlined={ true }>
                        Регистрация
                    </Heading.Heading>
                    <div className="sign-up__form-group">
                        <Label.Label htmlFor="email-field">
                            Никнейм:
                        </Label.Label>
                        <TextInput.TextInput 
                            required={ true } placeholder="Example username"
                            name="email-field"  
                        />
                    </div>
                    <div className="sign-up__form-group">
                        <Label.Label htmlFor="email-field">
                            Почта:
                        </Label.Label>
                        <TextInput.TextInput 
                            required={ true } placeholder="john@email.example"
                            name="email-field" type="email"
                        />
                    </div>
                    <div className="sign-up__form-group">
                        <Label.Label htmlFor="email-field">
                            Пароль:
                        </Label.Label>
                        <TextInput.TextInput 
                            required={ true }
                            name="email-field" type="password"
                        />
                    </div>
                    <div className="sign-up__form-group">
                        <Label.Label htmlFor="email-field">
                            Подтверждение пароля:
                        </Label.Label>
                        <TextInput.TextInput 
                            required={ true }
                            name="email-field" type="password"
                        />
                    </div>
                    <Button.Button>
                        Зарегистрироваться
                    </Button.Button>
                    <FlatButton.FlatButton>
                        У меня уже есть аккаунт
                    </FlatButton.FlatButton>
                </form>
            </div>
        </div>
    );
}

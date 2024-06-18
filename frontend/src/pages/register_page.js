import { useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { TextInput, PasswordInput } from '../ui/elements/inputs';
import { 
    LinkButtonPrimary, LinkButtonSecondary, BackButton,
} from '../ui/elements/buttons';
import { ErrorLabel } from '../ui/elements/labels.js';
import * as api from '../api/api.js';

import '../ui/elements/inputs.css';
import '../ui/elements/links.css';

export default function RegisterPage() {
    let token = new api.tokens.AuthToken('');

    let user_email = useRef();
    let user_nickname = useRef();
    let user_password = useRef();
    let user_password2 = useRef();

    let navigate = useNavigate();

    let [validFields, setValidFields] = useState({
        validEmail: true,
        validNickname: true,
        validPassword: true,
        passwordsSame: true,
        hasEmail: true,
        error: true,
    });

    function setValidFieldsAllTrue() {
        setValidFields({
            validEmail: true,
            validNickname: true,
            validPassword: true,
            passwordsSame: true,
            hasEmail: true,
            error: true,
        });
    }

    function changeValidFields(key, value) {
        let newValidFields = {
            validEmail: true,
            validNickname: true,
            validPassword: true,
            passwordsSame: true,
            hasEmail: true,
            error: true,
        };
        newValidFields[key] = value;
        setValidFields(newValidFields);
    }

    const [checkboxInputed, setCheckboxInputed] = useState(false);

    return (
        <>
            <Background>
                <Modal>
                    <BackButton />
                    <span className='header-text'>Регистрация</span>
                    <TextInput 
                        name='email' required={ true } 
                        placeholder='john@email.com' ref={ user_email }
                    >
                        Электронная почта
                    </TextInput>
                    <ErrorLabel hidden={ validFields.validEmail }>
                        Некорректная почта
                    </ErrorLabel>
                    <ErrorLabel hidden={ validFields.hasEmail }>
                        Почта или никнейм уже использованы
                    </ErrorLabel>
                    <TextInput 
                        name='nickname' required={ true } 
                        placeholder='ExampleNickname' ref={ user_nickname }
                    >
                        Никнейм
                    </TextInput>
                    <ErrorLabel hidden={ validFields.validNickname }>
                        Слишком короткий или слишком длинный никнейм
                    </ErrorLabel>
                    <ErrorLabel hidden={ validFields.hasEmail }>
                        Почта или никнейм уже использованы
                    </ErrorLabel>
                    <PasswordInput 
                        name='password' required={ true }
                        placeholder='1234' ref={ user_password }
                    >
                        Пароль
                    </PasswordInput>
                    <ErrorLabel hidden={ validFields.passwordsSame }>
                        Пароли не совпадают
                    </ErrorLabel>
                    <ErrorLabel hidden={ validFields.validPassword }>
                        Слишком короткий пароль
                    </ErrorLabel>
                    <PasswordInput
                        name='password2' required={ true }
                        placeholder='1234' ref={ user_password2 }
                    >
                        Подтверждение пароля
                    </PasswordInput>
                    <ErrorLabel hidden={ validFields.passwordsSame }>
                        Пароли не совпадают
                    </ErrorLabel>
                    <ErrorLabel hidden={ validFields.error }>
                        Внутренняя ошибка сервера. Пожалуйста, сообщите о ней
                        здесь: 
                        <a 
                          href='https://github.com/Minuta18/ChGK-helper/issues'
                        >
                            https://github.com/Minuta18/ChGK-helper/issues
                        </a>
                    </ErrorLabel>
                    <label className="form-label">
                        <input 
                            type="checkbox" className="input-checkbox" 
                            onChange={ 
                                e => setCheckboxInputed(e.target.checked)
                            } 
                        />
                        Я прочитал <a 
                            className="link"
                        >политику конфиденциальности</a> и <a 
                            className="link"
                        >условия пользования сервисом.</a>
                    </label>
                    <LinkButtonPrimary disabled={ !checkboxInputed } onClick={
                        () => {
                            setValidFieldsAllTrue();

                            if (user_password.current.value != 
                                user_password2.current.value) {
                                changeValidFields('passwordsSame', false);
                                return null;
                            }

                            api.users.createUser(
                                user_nickname.current.value,
                                user_email.current.value,
                                user_password.current.value
                            ).then((info) => {
                                const [statusCode, responseBody] = info;
                                // console.log(statusCode, responseBody);
                                if (statusCode === 201) {
                                    token.fetchToken(
                                        user_nickname.current.value,
                                        user_password.current.value,
                                        // There is some error handlers which 
                                        // haven't to work. If they work, we
                                        // will be in huuuge ass
                                        () => {}, () => {}, () => {}, () => {}
                                    );
                                    navigate('/home', { replace: true });
                                } else if (statusCode === 400) {
                                    if (responseBody.message === 'Invalid email') {
                                        changeValidFields('validEmail', false);
                                    } else if (responseBody.message === 'Invalid password') {
                                        changeValidFields('validPassword', false);
                                    } else if (responseBody.message === 'Invalid nickname') {
                                        changeValidFields('validNickname', false);
                                    } else if (responseBody.message === 'Email or Nickname already used') {
                                        changeValidFields('hasEmail', false);
                                    } 
                                    console.log(responseBody.message);
                                } else {
                                    console.error(statusCode, responseBody);
                                    changeValidFields('error', false);
                                }
                            });
                        }
                    }>
                        Регистрация
                    </LinkButtonPrimary>
                    <LinkButtonSecondary href='/auth/login'>
                        У меня уже есть аккаунт
                    </LinkButtonSecondary>
                </Modal>
            </Background>
        </>
    );
}

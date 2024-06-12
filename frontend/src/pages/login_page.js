import React from 'react';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { TextInput, PasswordInput } from '../ui/elements/inputs';
import { 
    LinkButtonPrimary, LinkButtonSecondary 
} from '../ui/elements/buttons';

export default function LoginPage() {
    return (
        <>
            <Background>
                <Modal>
                    <span className='header-text'>Вход</span>
                    <TextInput 
                        name='nickname' required={ true } 
                        placeholder='ExampleNickname'
                    >
                        Никнейм или почта
                    </TextInput>
                    <PasswordInput 
                        name='password' required={ true }
                        placeholder='1234'
                    >
                        Пароль
                    </PasswordInput>
                    <LinkButtonPrimary>Вход</LinkButtonPrimary>
                    <LinkButtonSecondary href='/auth/register'>
                        Зарегистрироваться
                    </LinkButtonSecondary>
                </Modal>
            </Background>
        </>
    );
}

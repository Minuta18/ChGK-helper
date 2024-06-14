import React from 'react';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { TextInput } from '../ui/elements/inputs';
import { 
    LinkButtonPrimary, LinkButtonSecondary, BackButton,
} from '../ui/elements/buttons';

export default function SettingsPage() {
    return (
        <>
            <Background>
                <Modal>
                    <BackButton />
                    <span className='header-text'>Настройки</span>
                    
                    
                    <TextInput 
                        name='reading_time' required={ true }
                        placeholder='0'
                        type='number'
                        min='0'
                    >
                        Время на чтение
                    </TextInput>

                    <TextInput 
                        name='solving_time' required={ true }
                        placeholder='0'
                        type='number'
                        min='0'
                    >
                        Время на решение
                    </TextInput>

                    <TextInput 
                        name='typing_time' required={ true }
                        placeholder='0'
                        type='number'
                        min='0'
                    >
                        Время на ввод ответа
                    </TextInput>


                    <LinkButtonPrimary>Сохранить</LinkButtonPrimary>
                    <LinkButtonSecondary href='/play'>
                        Отмена
                    </LinkButtonSecondary>
                </Modal>
            </Background>
        </>
    );
}
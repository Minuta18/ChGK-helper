import { useState, useCallback, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { TextInput, IntInput } from '../ui/elements/inputs';
import { 
    ButtonPrimary, LinkButtonSecondary, BackButton,
} from '../ui/elements/buttons';

import * as api from '../api/api.js';

export default function SettingsPage() {
    const [isLoading, isInvalidToken, token] = api.tokens.useToken();
    const [isLoadingFetch, setLoadingFetch] = useState(true);
    const [error, setError] = useState(false);
    const navigate = useNavigate();
    const [mainUserId, setMainUserId] = useState(0);

    const [tfr, setTmr] = useState(0);
    const [tfs, setTms] = useState(0);
    const [tft, setTmt] = useState(0);

    const readingRef = useRef();
    const solvingRef = useRef();
    const typingRef = useRef();

    const localUpdateSettings = async (
            userId, timeForReading, timeForSolving, timeForTyping,
        ) => {
            await api.settings.updateSettings(
                userId, token, 
                () => { navigate('/login', { replace: true, }) },
                () => { setError(true); },
                timeForReading, timeForSolving, timeForTyping
            );
    };

    useEffect(() => {
        const fetchSettings_ = async (
            userId,
        ) => {
            let settings = new api.settings.Settings();
            settings.fetchSettings(
                userId, token, () => {
                    navigate('/auth/login', { replace: true });
            }).then(([gtfr, gtfs, gtft]) => {
                setTmr(gtfr); setTms(gtfs); setTmt(gtft);
            });
        };
        
        api.users.getUserId(token, () => {
            navigate('/auth/login', { replace: true });
        }).then(
            (gottenUserId) => { 
                if (gottenUserId !== undefined) {
                    setMainUserId(gottenUserId);
                    console.log('Fetched user id: ', gottenUserId);
                    fetchSettings_(gottenUserId).then(() => {
                        setLoadingFetch(false); 
                    });
                }
            }
        );
    }, []);

    return (
        <>
            <Background>
                <Modal>
                    { isLoading || isLoadingFetch ? <p>Загрузка</p> :
                        <>
                            <BackButton />
                            <span className='header-text'>Настройки</span>
                            
                            <IntInput
                                name='reading_time' required={ true }
                                placeholder='0'
                                type='number' 
                                defValue={ tfr }
                                min='0' ref={ readingRef }
                            >
                                Время на чтение
                            </IntInput>
                            <IntInput 
                                name='solving_time' required={ true }
                                placeholder='0'
                                type='number' 
                                defValue={ tfs }
                                min='0' ref={ solvingRef }
                            >
                                Время на решение
                            </IntInput>

                            <IntInput 
                                name='typing_time' required={ true }
                                placeholder='0'
                                type='number' 
                                defValue={ tft }
                                min='0' ref={ typingRef }
                            >
                                Время на ввод ответа
                            </IntInput>

                            <ButtonPrimary 
                                onClick={
                                    async () => {
                                        localUpdateSettings(
                                            mainUserId,
                                            readingRef.current.value,
                                            solvingRef.current.value,
                                            typingRef.current.value,
                                        ).then(() => {
                                            setTmr(readingRef.current.value); 
                                            setTms(solvingRef.current.value); 
                                            setTmt(typingRef.current.value);
                                        });
                                    }
                                }
                            >Сохранить</ButtonPrimary>
                        </>
                    }
                </Modal>
            </Background>
        </>
    );
}

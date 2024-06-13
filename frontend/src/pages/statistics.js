import React from 'react';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { 
    LinkButtonPrimary, LinkButtonSecondary, BackButton,
} from '../ui/elements/buttons';

export default function Statistics(props) {

    return (
        <>
            <Background>
                <Modal>
                    <BackButton />
                    <span className='header-text'>Статистика</span>
                    { props.stats.map(() => 
                        <span> Ваш ответ:{props.stats.answer} Верный ответ:{props.stats.corr_sanswer} </span>
                    ) }
                </Modal>
            </Background>
        </>
    );
}
import React from 'react';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { 
    LinkButtonPrimary, LinkButtonSecondary, BackButton,
} from '../ui/elements/buttons';

export default function Statistics(props) {
    console.log(props)
    return (
        <>
            <Background>
                <Modal>
                    <span className='header-text'>Статистика</span>
                    { props.stats.map(q => 
                        <span> #{q.num}: { q.solve ?
                            <span className='green-font'>Решён</span> : 
                            <span className='red-font'>Не решён</span>
                        } </span>
                    ) }
                    <LinkButtonPrimary href='/home'>
                        На главную
                    </LinkButtonPrimary>
                </Modal>
            </Background>
        </>
    );
}
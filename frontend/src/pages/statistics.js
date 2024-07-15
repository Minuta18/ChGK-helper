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
                    <div className='height-limit'>
                        { props.stats.map(q => 
                            <div> #{q.num}: 
                                { q.solve === 'solved' ? 
                                (<span className='green-font'>Решён</span>) :
                                <></>}
                                { q.solve === 'not solved' ? 
                                (<span className='red-font'>Не решён</span>) :
                                <></>}
                                { q.solve === 'skipped' ? 
                                (<span>Пропущен</span>) :
                                <></>}
                            </div>
                        ) }
                    </div>
                    <LinkButtonPrimary href='/'>
                        На главную
                    </LinkButtonPrimary>
                </Modal>
            </Background>
        </>
    );
}
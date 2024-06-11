import React from 'react';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';

export default function MainPage() {
    return (
        <>
            <Background>
                <Modal><span className='header-text'>Hello world</span></Modal>
            </Background>
        </>
    );
}
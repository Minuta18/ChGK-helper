import React from 'react';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { 
    LinkButtonPrimary, LinkButtonSecondary, BackButton,
} from '../ui/elements/buttons';

export default function Home() {
    return (
        <>
            <Background>
                <Modal>
                    <BackButton />
                </Modal>
            </Background>
        </>
    );
}
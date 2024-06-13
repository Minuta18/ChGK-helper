import React from 'react';

import { Question } from '../ui/elements/question.js';
import Background from '../ui/containers/background.js';
import Modal from '../ui/containers/modal.js';
import { BackButton } from '../ui/elements/buttons.js';

import * as api from '../backend-lib/questions.js';

export default function QuestionsPage() {
    let question = new api.Question('random');
    
    return (<>
        <Background>
            <Modal>
                {/* <BackButton /> */}
                <Question id={ 2 } num={ 1 } tfr={ 5 } 
                    tfs={ 10 } tft={ 15 }
                >
                    Почему Михаил не работает?
                </Question>
            </Modal>
        </Background>
    </>);
}

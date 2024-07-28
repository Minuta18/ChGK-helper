import React from 'react';

import { Header } from '../../../widgets/header/index';
import * as Kit from '../../../shared/kit/index';
import { MainPanel } from '../../../widgets/mainPanel/ui/mainPanel';
import { NewsPanel } from '../../../widgets/newsPanel';
import { Footer } from '../../../widgets/footer/index';

export function IndexPage() {
    return (
        <Kit.PageLayout 
            header={<Header />} 
            aside={<Kit.Container>
                    <NewsPanel />
            </Kit.Container>} 
            mainContent={<Kit.Container>
                <MainPanel />
            </Kit.Container>}
            footer={<Footer />}
        />
    );
}

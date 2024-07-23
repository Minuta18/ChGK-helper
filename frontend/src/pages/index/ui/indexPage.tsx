import React from 'react';

import { Header } from '../../../widgets/header/index';
import { PageLayout } from '../../../shared/kit/pageLayout/index';
import { Container } from '../../../shared/kit/container/index';
import { MainPanel } from '../../../widgets/mainPanel/ui/mainPanel';
import { NewsPanel } from '../../../widgets/newsPanel';
import { Footer } from '../../../widgets/footer/index';

export function IndexPage() {
    return (
        <PageLayout 
            header={<Header />} 
            aside={<Container>
                    <NewsPanel />
            </Container>} 
            mainContent={<Container>
                <MainPanel />
            </Container>}
            footer={<Footer />}
        />
    );
}

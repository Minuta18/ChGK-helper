import React from 'react';

import { Header } from '../../../widgets/header/index';
import { PageLayout } from '../../../shared/kit/pageLayout/index';
import { Container } from '../../../shared/kit/container/index';

export function IndexPage() {
    return (
        <PageLayout 
            header={<Header />} 
            aside={<Container>amogus</Container>} 
            mainContent={<Container>sus</Container>}
        />
    );
}

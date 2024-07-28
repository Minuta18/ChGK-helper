import * as React from "react";

import { PageLayout } from '../../../shared/kit/pageLayout/index';
import { Header } from '../../../widgets/header/index';
import { Container } from '../../../shared/kit/container/index';
import { Footer } from '../../../widgets/footer/index';
import { SignUpPanel } from "../../../widgets/signUpPanel";

export function SignUpPage() {
    return (
        <PageLayout 
            header={<Header />}
            form={<Container style={{
                padding: 0,
                display: "flex",
                flexDirection: "row",
            }}>
                <SignUpPanel />
            </Container>}
            footer={<Footer />}
        />
    );
}

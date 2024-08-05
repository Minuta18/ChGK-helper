import * as React from "react";

import * as Kit from '../../../shared/kit/index';
import { Header } from '../../../widgets/header/index';
import { Footer } from '../../../widgets/footer/index';
import { SignUpPanel } from "../../../widgets/signUpPanel";

export function SignUpPage() {
    return (
        <Kit.PageLayout 
            header={<Header />}
            form={<Kit.Container style={{
                padding: 0,
                display: "flex",
                flexDirection: "row",
            }}>
                <SignUpPanel />
            </Kit.Container>}
            footer={<Footer />}
        />
    );
}

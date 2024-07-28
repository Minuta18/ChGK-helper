import * as React from "react";

import * as Kit from '../../../shared/kit/index';
import { Header } from '../../../widgets/header/index';
import { Footer } from '../../../widgets/footer/index';
import { SignInPanel } from "../../../widgets/signInPanel";

export function SignInPage() {
    return (
        <Kit.PageLayout 
            header={<Header />}
            form={<Kit.Container style={{
                padding: 0,
                display: "flex",
                flexDirection: "row",
            }}>
                <SignInPanel />
            </Kit.Container>}
            footer={<Footer />}
        />
    );
}

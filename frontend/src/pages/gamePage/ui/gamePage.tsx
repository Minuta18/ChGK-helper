import * as React from "react";

import * as Kit from "../../../shared/kit/index";
import { Header } from "../../../widgets/header/index";
import { Footer } from "../../../widgets/footer/index";
import { QuestionList } from "../../../widgets/questionList/index";

export function GamePage() {
    return (
        <Kit.PageLayout 
            header={<Header />}
            aside={<QuestionList />}
            mainContent={<Kit.Container>

            </Kit.Container>}
            footer={<Footer />}
        />
    );
}

export enum QuestionStatus {
    SOLVED,
    FAILED,
    SKIPPED,
    IN_PROGRESS,
}

export type Question = {
    text?: string;
    comment?: string;
    correct_answer?: string;
    status?: QuestionStatus;    
    id?: number;
}

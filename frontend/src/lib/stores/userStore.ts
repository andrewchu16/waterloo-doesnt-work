// userStore.ts
import { persistToLocalStorage } from '../localStorageUtil';

export type SeasonAvailable = "winter 2025" | "summer 2025" | "fall 2025" | "spring 2025";

export interface User {
    Name: string;
    Email: string;
    Ethnicity: string[];
    Age: number | null;
    resumeSummary: string;
    Education: string;
    GraduationYear: number | null;
    seasonAvailable: SeasonAvailable;
    Experiences: string[];
}

// Initial value for the user
const initialUser: User = {
    Name: '',
    Ethnicity: [],
    Age: null,
    resumeSummary: '',
    Education: '',
    GraduationYear: null,
    seasonAvailable: 'winter 2025',
    Experiences: [],
};

// Create a writable store that persists to localStorage
export const user = persistToLocalStorage<User>('userStore', initialUser);

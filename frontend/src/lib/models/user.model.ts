import type { SeasonAvailable } from './seasonAvailability.model';

export interface User {
	name: string;
	email: string;
	ethnicity: string[];
	resumeSummary: string;
	education: string;
	graduationYear: number | null;
	seasonAvailable: SeasonAvailable;
}

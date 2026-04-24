export interface User {
  id: string;
  email: string;
  username: string;
  displayName?: string;
  isActive: boolean;
}

export interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
}

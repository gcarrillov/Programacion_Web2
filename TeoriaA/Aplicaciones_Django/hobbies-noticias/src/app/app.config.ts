import { provideRouter, Routes } from '@angular/router';
import { Hobbies } from './pages/hobbies/hobbies';
import { News } from './pages/news/news';
import { About } from './pages/about/about';

const routes: Routes = [
  { path: '', redirectTo: 'hobbies', pathMatch: 'full' },
  { path: 'hobbies', component: Hobbies },
  { path: 'news', component: News },
  { path: 'about', component: About }
];

export const appConfig = {
  providers: [provideRouter(routes)],
};

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TopicsComponent } from './topics/topics.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { TopicArticlesComponent } from './topic-articles/topic-articles.component';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full'},
  { path: 'topics', component: TopicsComponent },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'articles/:name', component: TopicArticlesComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes)],
  exports: [ RouterModule ]
})
export class AppRoutingModule {
}

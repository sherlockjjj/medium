import { Injectable } from '@angular/core';
import { Topic } from './topic';
import { Observable, of } from 'rxjs';
import { MessageService } from './message.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
import { Article } from './article';

@Injectable({
  providedIn: 'root'
})

export class TopicService {
  private mainUrl = 'http://localhost:3000';
  private topicsUrl = this.mainUrl + '/api/topics';
  private articlesUrl = this.mainUrl + '/api/articles';

  constructor(
    private messageService: MessageService,
    private http: HttpClient) {}

  private log(message: string) {
    this.messageService.add(`TopicService: ${message}`);
  }

  getTopics() {
    return this.http.get<{topics: any}>(this.topicsUrl)
    .pipe(map((topicData) => {
      return topicData.topics.map(topic => {
        return {
          name: topic.name,
          id: topic._id
        };
      });
    }));
  }

  getTopic(topic: string) {
    const url = `${this.articlesUrl}/${topic}`;
    return this.http.get<{articles: any}>(url)
    .pipe(map((topicData) => {
      return topicData.articles.map(article => {
        return {
          title: article.title,
          id: article._id,
          tag: article.tag,
          author: article.author,
          publish_time: article.publish_time,
          url: article.url,
          author_url: article.author_url,
          headings: article.headings,
          contents: article.contents,
          min_read: article.min_read,
          claps: article.claps
        };
      });
    }));
  }
}

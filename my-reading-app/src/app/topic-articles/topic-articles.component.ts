import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { TopicService } from '../topic.service';
import { Article } from '../article';

@Component({
  selector: 'app-topic-articles',
  templateUrl: './topic-articles.component.html',
  styleUrls: ['./topic-articles.component.css']
})

export class TopicArticlesComponent implements OnInit {
  @Input() articles: Article[];

  constructor(
    private route: ActivatedRoute,
    private topicService: TopicService,
    private location: Location
  ) { }

  ngOnInit() {
    this.getTopic();
  }

  getTopic() {
    const name = this.route.snapshot.paramMap.get('name');
    console.log(name);
    this.topicService.getTopic(name)
    .subscribe(articles => this.articles = articles);
  }

  goBack(): void {
    this.location.back();
  }
}

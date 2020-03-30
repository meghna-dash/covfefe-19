/*global chrome*/
import React, { Component } from 'react';
import { Badge, Button, Card, CardImg, CardText, CardBody, CardTitle, CardSubtitle, Col, Row } from 'reactstrap';
let psl = require('psl');

class LinkCard extends Component {
 constructor(props) {
   super(props);
   this.goToLink = this.goToLink.bind(this);
 }

 goToLink() {
   chrome.tabs.create({ url: this.props.link });
 }

 extractHostname(url) {
    var hostname;
    if (url.indexOf("//") > -1) {
        hostname = url.split('/')[2];
    }
    else {
        hostname = url.split('/')[0];
    }
    hostname = hostname.split(':')[0];
    hostname = hostname.split('?')[0];
    return hostname;
  }

 render() {
   return (
     <div>
       <Card
          className="link-card"
          onClick={this.goToLink}
        >
          <CardBody>
            <CardText>
              <h2>
                {psl.get(this.extractHostname(this.props.link))}
              </h2>
              <h3>
                {this.props.title}
                {' '}
                <span class="msc-badge msc-badge__success">
                  {Math.round(this.props.similarity * 100)}% similar
                </span>
              </h3>
              {this.props.description}
            </CardText>
          </CardBody>
      </Card>
      <br/>
    </div>
  )
 }
}

export default LinkCard;

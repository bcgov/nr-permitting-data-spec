---
layout: default
name: HOME
---
{% assign carouselCards = site.overview | where: "type", "carousel" | sort: 'order' %}
{% assign iconCards = site.overview | where: "type", "icon" | sort: 'order' %}
{% assign checkerboardCards = site.overview | where: "type", "checkerboard" | sort: 'order' %}
{% assign commonServices = site.services | sort: 'order' %}

<div class="container">
  <div id="overviewCarousel" class="carousel slide" data-ride="carousel">
    <ol class="carousel-indicators">
      {% for card in carouselCards %}
        <li data-target="#overviewCarousel" data-slide-to="{{ forloop.index | minus: 1 }}" class="{% if forloop.index == 1 %} active{% endif %}"></li>
      {% endfor %}
    </ol>
    <div class="carousel-inner">
      {% for card in carouselCards %}
      <div class="carousel-item {% if forloop.index == 1 %} active{% endif %}">
        <div class="row">
          <div class="col-sm-5 carousel-card-text">
            <h4 class="carousel-card-header">{{ card.title }}</h4>
            <p>{{ card.content }}</p>
          </div>
          <div class="col-sm-7">
            <img class="img-fluid " src="{{ site.baseurl }}{{ card.img.path }}" alt="{{ card.img.alt }}">
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
    <a class="carousel-control-prev" href="#overviewCarousel" role="button" data-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#overviewCarousel" role="button" data-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>

  <div class="mb-3 mt-5 px-5">
    <p>This website provides information relating to a range of services and open-source software components created by the Common Service Showcase team. We aim to promote, curate, develop, and make it easy to onboard to our hosted services or integrate our micro-services and common components into your own applications. The goal is to <strong>reduce costs, accelerate development, and promote consistency</strong> and supportability of BC Gov digital services.</p>
    
    <!-- Integrated Wiki Content -->
    <div class="wiki-content">
      # Natural Resource Common Permitting Data Specifications

      [![lifecycle:maturing](https://img.shields.io/badge/Lifecycle-Maturing-007EC6)](https://github.com/bcgov/repomountie/blob/master/doc/lifecycle-badges.md)
      [![Contributions:Welcome](https://img.shields.io/badge/Contributions-Welcome-green)](https://github.com/bcgov/nr-permitting-data-spec/issues)
      ![Data:Schema](https://img.shields.io/badge/Data-Schema-aqua)

      ## Description
      This repository contains common schemas related to permitting in the Natural Resources Sector. 

      The intent of these are to standardize the way permitting in the Natural Resource Sector is described as data to enable quality and interoperability.

      Hosting these will enable and ensure version history will be maintained.

      These will be reviewed as required with the related data managers and permitting teams.

      ## Purpose

      The common specifications are to

      * create cross sector data governance
      * feed intelligence to the sector
      * moving towards harmonized statuses 
      * activity-based permit bundling
      * and application process tracking
      * enable consistent collection of data and metadata
      * leverage for an integrated data schema for reporting and analytics
      * identify opportunities on data quality, data visualizations, and gaps
      * develops data patterns and guidelines
      * develop common schema patterns for other areas like First Nations Consultation

      ## Overview

      ### Schemas

      | Subject | Description |JSON| DOC| 
      | --- | --- | --- | --- |
      | Core Specification | The core permitting content, structure, data types, and expected enums that are consistent across all permitting datasets. | [json](core-permit-schema.json)| [doc](core-permit-schema.md) | 
      | Housing Specification | The housing specific schema elements that extend the core schema. | [json](housing-permit-schema.json)| [doc](housing-permit-schema.md)|
      | Metadata Specification |The metadata elements required and captured while discovering and onboarding into an integrated dataset. |[json](metadata-discovery-schema.json) |[doc](metadata-discovery-schema.md)  |
      | Permit Name Registry Specification |This spec is to enable the registry of permit names from source systems/information to be used as enums in the core Core Specification. |[json](permit-name-registry-schema.json) |[doc](permit-name-registry-schema.md)  |

      ### Scripts

      | Subject | Description |Readme|
      | --- | --- | --- |
      | Validation | This package takes a JSON document and validates it against an expected schema structure as defined in a JSON schema definition file. |[readme](https://github.com/bcgov/nr-permitting-data-spec/blob/630b56ce631adf02dc819ec54bd710cc1e57276e/tools/schemas/validation/README.md) |
      | Auto-generation of docs | This package converts JSON schema definition files into markdown files. | [readme](https://github.com/bcgov/nr-permitting-data-spec/blob/630b56ce631adf02dc819ec54bd710cc1e57276e/tools/autogen/docs/README.md) |

      ## Future

      * Complete data dictionaries
      * Finalize status and states terms

      ### Schemas
      * status and state registries 
          * To enable the mapping of source values to a standardized list
      * activity bundling
          * To enable identifying what permits are applicable to an activity on the landbase, e.g., housing, mining, connectivity.
      * client/proponent
      * other permitting initiatives

      ### Design

      Along with the data specification will be the design presentation to enable a common look and feel.
    </div>
    
    <div class="row">
      {% for card in iconCards %}
      <div class="icon-list col-sm-4">
          <img class="img-fluid" src="{{ site.baseurl }}{{ card.img.path }}" alt="{{ card.img.alt }}">
          {{ card.content}}
      </div>
      {% endfor %}
    </div>
  </div>
  <div class="checkerboard mb-5">
    {% for card in checkerboardCards %}
    <div class="row">
      <div class="col-sm-4 check-title d-flex justify-content-center align-items-center">
          {{ card.title }}
      </div>
      <div class="col-sm-8 check-content">
          {{ card.content }}
      </div>
    </div>
    {% endfor %}
  </div>
  <div class="text-center my-5">
    <h3 class="title-text" id="home-component-cards"> <img class="img-fluid mr-3" src="{{ site.baseurl }}/assets/images/developer_board.svg" alt="components"> <strong>Available Common Components</strong></h3>
  </div>
  <div class="mb-5 service-card-list">
    <div class="row">
      {% for card in commonServices %}
      <div class="col-md-6">
        <a class="linked-card" href="{{ site.baseurl }}{{ card.url }}.html">
          <div class="card">
            <div class="card-body">
              <div class="row">
                <div class="col-10 col-xl-11">
                  <h3 class="card-title">{{ card.title }} ({{ card.name }}) {{ card.version }}</h3>
                </div>
                <div class="col-2 col-xl-1 text-right">
                  <i class="fa fa-lg fa-arrow-circle-right"></i>
                </div>
              </div>
              <strong>Onboarding Options:</strong>
              <br />
              <ul class="service-onboard">
                {% for onb in card.onboard %}
                  <li>{{ onb }}</li>
                {% endfor %}
              </ul>
            </div>
          </div>
        </a>
      </div>
      {% endfor %}
    </div>
  </div>
</div>

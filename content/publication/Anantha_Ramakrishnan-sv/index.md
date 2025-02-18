---
title: 'ANNA: Abstractive Text-to-Image Synthesis with Filtered News Captions'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Aashish Anantha Ramakrishnan
  - Sharon X Huang
  - Dongwon Lee

# Author notes (optional)
# author_notes:
#   - 'Equal contribution'
#   - 'Equal contribution'

date: '2024-07-01T00:00:00Z'
doi: 'https://doi.org/10.48550/arXiv.2301.02160'

# Schedule page publish date (NOT publication's date).
# publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *ACL 3rd Workshop on Advances in Language and Vision Research (ALVR)*
publication_short: In *ACL-W ALVR 2024*

abstract: Advancements in Text-to-Image synthesis over recent years have focused more on improving the quality of generated samples on datasets with descriptive captions. However, real-world image-caption pairs present in domains such as news data do not use simple and directly descriptive captions. With captions containing information on both the image content and underlying contextual cues, they become abstractive in nature. In this paper, we launch ANNA, an Abstractive News captioNs dAtaset extracted from online news articles in a variety of different contexts. We explore the capabilities of current Text-to-Image synthesis models to generate news domain-specific images using abstractive captions by benchmarking them on ANNA, in both standard training and transfer learning settings. The generated images are judged on the basis of contextual relevance, visual quality, and perceptual similarity to ground-truth image-caption pairs. Through our experiments, we show that techniques such as transfer learning achieve limited success in understanding abstractive captions but still fail to consistently learn the relationships between content and context features.

# Summary. An optional shortened abstract.
summary: In this paper, we launch ANNA, an Abstractive News captioNs dAtaset extracted from online news articles in a variety of different contexts. Through our experiments, we show that techniques such as transfer learning achieve limited success in understanding abstractive captions but still fail to consistently learn the relationships between content and context features.

tags: []

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
links:
- name: Arxiv
  url: https://arxiv.org/abs/2301.02160

# url_pdf: ''
# url_code: 'https://github.com/HugoBlox/hugo-blox-builder'
url_dataset: https://github.com/aashish2000/ANNA
# url_poster: ''
# url_project: ''
# url_slides: ''
# url_source: 'https://github.com/HugoBlox/hugo-blox-builder'
# url_video: 'https://youtube.com'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# image:
  # caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  # focal_point: ''
  # preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects:
#   - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---

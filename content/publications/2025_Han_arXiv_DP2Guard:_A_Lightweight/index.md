---
title: "DP2Guard: A Lightweight and Byzantine-Robust Privacy-Preserving Federated Learning Scheme for Industrial IoT"
date: 2025-01-01
publishDate: 2025-01-01
authors: ["**Baofu Han**", "Bing Li", "Yining Qi", "Raja Jurdak", "Kaibin Huang", "Chau Yuen"]
publication_types: ["3"]
abstract: "Privacy-Preserving Federated Learning (PPFL) has emerged as a secure distributed Machine Learning (ML) paradigm that aggregates locally trained gradients without exposing raw data. To defend against model poisoning threats, several robustness-enhanced PPFL schemes have been proposed by integrating anomaly detection. Nevertheless, they still face two major challenges: (1) the reliance on heavyweight encryption techniques results in substantial communication and computation overhead; and (2) single-strategy defense mechanisms often fail to provide sufficient robustness against adaptive adversaries. To overcome these challenges, we propose DP2Guard, a lightweight PPFL framework that enhances both privacy and robustness. DP2Guard leverages a lightweight gradient masking mechanism to replace costly cryptographic operations while ensuring the privacy of local gradients. A hybrid defense strategy is proposed, which extracts gradient features using singular value decomposition and cosine similarity, and applies a clustering algorithm to effectively identify malicious gradients. Additionally, DP2Guard adopts a trust score-based adaptive aggregation scheme that adjusts client weights according to historical behavior, while blockchain records aggregated results and trust scores to ensure tamper-proof and auditable training. Extensive experiments conducted on two public datasets demonstrate that DP2Guard effectively defends against four advanced poisoning attacks while ensuring privacy with reduced communication and computation costs."
featured: true
publication: "arXiv 2025 "
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'https://arxiv.org/abs/2507.16134'
---

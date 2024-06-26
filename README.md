# Theoretical analysis of user simulation objective

This repository contains the code and data used to generate the results presented within the following the paper:

> N. Bernard and K. Balog. **Towards a Formal Characterization of User Simulation Objectives in Conversational Information Access**. In: Proceedings of the 2024 ACM SIGIR International Conference on the Theory of Information Retrieval (ICTIR '24). 2024. [[DOI: 10.1145/3664190.3672529](https://doi.org/10.1145/3664190.3672529)]

## Summary

User simulation is a promising approach for automatically training and evaluating conversational information access agents, enabling the generation of synthetic dialogues and facilitating reproducible experiments at scale. However, the objectives of user simulation for the different uses remain loosely defined, hindering the development of effective simulators.
In this work, we formally characterize the distinct objectives for user simulators: training aims to maximize behavioral similarity to real users, while evaluation focuses on the accurate prediction of real-world conversational agent performance.
Through an empirical study, we demonstrate that optimizing for one objective does not necessarily lead to improved performance on the other. This finding underscores the need for tailored design considerations depending on the intended use of the simulator.
By establishing clear objectives and proposing concrete measures to evaluate user simulators against those objectives, we pave the way for the development of simulators that are specifically tailored to their intended use, ultimately leading to more effective conversational agents.

## Repository Organization

This repository is structured as follows:

  - `data/annotated_datasets`: Contains the datasets annotated following the QRFA model.
  - `ictir_2024_experimentation.ipynb`: Jupyter notebook with the code used to generate the results presented in the paper.

## Citation

If you use this code or data, please cite the following paper:

```bibtex
@inproceedings{Bernard:2024:ICTIR,
  author      = {Bernard, Nolwenn and Balog, Krisztian},
  booktitle   = {Proceedings of the 2024 ACM SIGIR International Conference on the Theory of Information Retrieval},
  title       = {Towards a Formal Characterization of User Simulation Objectives in Conversational Information Access},
  year        = {2024},
  doi         = {10.1145/3664190.3672529},
  series ={ICTIR '24}
}
```

## Contact

Should you have any questions, please contact Nolwenn Bernard at <nolwenn.m.bernard@uis.no>.

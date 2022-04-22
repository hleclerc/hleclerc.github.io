# Cluster de calcul

## Composition

Le cluster se compose de 9 machines avec les capacités suivantes :

| Nom    | CPUs                     | Mem     |  GPUs                                  |
| ----   | -----------------------  | -----   | -------------------------------------- |
| node11 | 2x8  Sandy Bridge (avx)  | 256  Go | 1 x Tesla K20m (5 Go, 3.524 TFLOPS)    |
| node12 | 4x10 Broadwell (avx2)    | 128  Go | -                                      |
| node13 | 4x20 Skylake (avx2)      | 384  Go | -                                      |
| node14 | 2x64 Zen 3 (avx2)        | 1024 Go | -                                      |
| node15 | 2x28 Cascade Lake (avx2) | 768  Go | 1 x Quadro GV100 (32 Go, 16.66 TFLOPS) |
| node16 | 2x10 Ivy Bridge (avx)    | 64   Go | -                                      |
| node17 | 4x16 Broadwell (avx2)    | 256  Go | -                                      |
| node18 | 2x8  Sandy Bridge (avx)  | 192  Go | 1 x Tesla K20m (5 Go, 3.524 TFLOPS)    |
| node19 | 2x6  Nehalem (sse4_2)    | 35   Go | -                                      |

<!-- obtenu avec srun --nodelist=node11 ./pinxi --tty -Fxz -->

Vous trouverez des graphiques sur l’utilisation des différents nœuds (RAM, CPU,...) sur la [page ganglia](https://cinaps.imo.universite-paris-saclay.fr/), 

## Correspondants

Pour toute question technique non couverte ou peu claire dans la documentation, vous pouvez contacter:
* Benjamin.Auder@math.u-psud.fr (bureau 2A3)
* Sylvain.Faure@math.u-psud.fr (bureau 2D3)
* Hugo.Leclerc@math.u-psud.fr (bureau 2A3)
* Suzanne.Varet@math.u-psud.fr (bureau 2D3)

# optimal-strategy
Algorithm of searching for an optimal control of specific queuing system.

The properties of the queuing system:
- one server
- Poisson arrival with a rate of `lambda > 0`
- constant service time `c > 0`
- places for waiting `k > 0`
- income for every client `d > 0`
- loss for every waiting client with proportional coefficient `r > 0`
- number of actions

The program returns an optimal strategy and a vector of rewards.

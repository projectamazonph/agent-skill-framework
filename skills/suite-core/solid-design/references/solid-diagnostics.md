# SOLID Diagnostics

Use this reference to diagnose architecture or justify a refactor. Treat every smell as a prompt to investigate, not automatic proof of a violation.

## Diagnostic Matrix

| Principle | Investigate when | Ask | Typical correction | Proof |
| --- | --- | --- | --- | --- |
| SRP | One module mixes policy, I/O, formatting, persistence, or unrelated actors | Which change requests cause this code to move? | Extract a focused policy, adapter, formatter, or coordinator | Focused unit tests plus unchanged integration behavior |
| OCP | Each new variant adds another branch to stable policy | Is there one known dimension of variation? | Strategy, handler, registry, plugin, composition, or data table | Add a variant without editing the stable decision algorithm |
| LSP | A subtype rejects valid inputs, changes semantics, or disables inherited methods | Can every valid base-type caller use it unchanged? | Correct the contract, narrow the interface, or replace inheritance with composition | Shared contract tests against every implementation |
| ISP | Implementers depend on or fake methods they do not need | Which exact capabilities does each client consume? | Split consumer-owned capability contracts and compose them | Compile/type checks and client-focused tests |
| DIP | Business rules import databases, vendors, frameworks, clocks, or global services | Which layer owns policy, and which detail is volatile? | Define a policy-owned port and boundary adapter; inject it | Unit tests with a fake plus adapter integration tests |

## SRP Diagnostics

### Strong evidence

- The same file changes for independent business actors or policies.
- Domain decisions cannot be tested without network, database, or UI setup.
- Formatting or transport changes repeatedly modify business calculations.
- One component owns multiple lifecycles with different release cadences.

### Weak evidence

- The file is long.
- The class has many methods.
- Its name contains “Manager” or “Service.”
- Several private helpers support one cohesive algorithm.

### Correction pattern

Keep the use-case coordinator thin but explicit:

```text
PlaceOrder
  -> PricingPolicy
  -> InventoryPort
  -> PaymentPort
  -> ReceiptPresenter
```

The coordinator's single responsibility is executing the place-order use case. Calling several collaborators does not itself violate SRP.

## OCP Diagnostics

### Strong evidence

- A stable switch statement changes every time a payment type, export format, or pricing policy is added.
- Independent feature teams edit the same central decision file for their variants.
- Adding a variant risks regressions in unrelated variants.

### Weak evidence

- A small exhaustive match over a closed domain enum.
- A branch expresses a core invariant that must remain centralized.
- Only one implementation exists and no variation is required.

### Correction pattern

```ts
interface DiscountPolicy {
  quote(input: QuoteInput): Money;
}

class QuoteService {
  constructor(private readonly discount: DiscountPolicy) {}

  quote(input: QuoteInput): Money {
    return this.discount.quote(input);
  }
}
```

Add a new `DiscountPolicy` implementation without altering `QuoteService`. Keep wiring in the composition root.

## LSP Diagnostics

Model the base contract before judging substitution:

| Contract element | Invalid subtype change |
| --- | --- |
| Accepted input | Rejects input valid for the base type |
| Returned result | Drops guarantees or changes units/meaning |
| Errors | Throws a new error for a valid base operation |
| State | Breaks invariants callers rely on |
| Side effects | Silently skips or adds material effects |
| Ordering | Reorders results when order is guaranteed |

### Contract-test pattern

```ts
function paymentGatewayContract(create: () => PaymentGateway) {
  test("charges a valid positive amount exactly once", async () => {
    const gateway = create();
    const result = await gateway.charge(validCharge);
    expect(result.status).toBe("approved");
  });
}

paymentGatewayContract(() => new StripeGateway(testClient));
paymentGatewayContract(() => new SandboxGateway());
```

If one implementation cannot pass the same valid contract, change the hierarchy or contract rather than weakening the test.

## ISP Diagnostics

### Strong evidence

- Methods throw `UnsupportedOperation`, return meaningless defaults, or remain empty.
- Read-only clients receive mutation methods.
- Implementing one capability requires importing unrelated frameworks.
- A small consumer mock must fake many irrelevant methods.

### Correction pattern

```ts
interface OrderReader {
  get(id: OrderId): Promise<Order | null>;
}

interface OrderWriter {
  save(order: Order): Promise<void>;
}

type OrderRepository = OrderReader & OrderWriter;
```

Accept `OrderReader` where only reads occur. Compose both capabilities only for clients that need both.

## DIP Diagnostics

### Strong evidence

- Domain code imports an SDK, ORM entity, HTTP request, or framework context.
- Business tests require real infrastructure.
- Time, randomness, IDs, environment variables, or global state produce nondeterministic policy behavior.
- A vendor change requires editing business rules.

### Correction pattern

```ts
interface OrderStore {
  save(order: Order): Promise<void>;
}

class SubmitOrder {
  constructor(
    private readonly store: OrderStore,
    private readonly clock: Clock,
  ) {}
}

class PostgresOrderStore implements OrderStore {
  // Translate between domain values and database records here.
}
```

The use-case layer owns `OrderStore`; the database adapter depends on that contract. Construct both at the application's outer edge.

## Common Misapplications

### Interface for every class

Reject when the interface has one implementation, no test or architectural seam, and merely mirrors the concrete class. Introduce the abstraction at the consumer boundary only when it isolates meaningful volatility.

### Excessive micro-classes

Reject when a cohesive algorithm is scattered across files and navigation cost exceeds separation value. SRP concerns reasons to change, not line count.

### Inheritance used only for reuse

Prefer composition when subclasses are not true semantic substitutes. Reuse is not evidence of an “is-a” relationship.

### Generic repository for every entity

Reject when domain queries, consistency rules, and transaction boundaries differ. Use consumer-specific ports that express actual use cases.

### Dependency injection container inside business logic

Reject service location. Resolve dependencies once at the composition root and pass them explicitly.

### Premature plugin systems

Keep a direct implementation until variation is required or strongly evidenced. A two-branch conditional is often clearer than a framework designed for imaginary plugins.

## Review Scoring Rubric

Score only with cited evidence.

| Score | Meaning |
| --- | --- |
| 0 | Material violation creates correctness, testability, or change-risk problems |
| 1 | Mixed design; boundary exists but leaks or creates avoidable coupling |
| 2 | Principle is satisfied proportionally to current requirements |
| N/A | Principle is not meaningfully exercised in the reviewed scope |

For each applicable principle, record:

1. Evidence: file, symbol, behavior, and dependency.
2. Consequence: concrete failure mode or maintenance cost.
3. Correction: smallest safe change.
4. Verification: exact unit, contract, integration, or architecture test.

Do not total the scores into a universal quality grade. A severe LSP defect can matter more than several clean interfaces.

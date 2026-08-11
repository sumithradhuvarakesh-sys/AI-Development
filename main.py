from planner import create_plan, observe_page
from tools import search_web, fetch_page
from logger import log_step

MAX_ITERATIONS = 5


def run_agent(user_input):

    print("User:", user_input)

    query = user_input

    for iteration in range(1, MAX_ITERATIONS + 1):

        print("\n==============================")
        print("Iteration:", iteration)
        print("==============================")

        # PERCEIVE
        print("\nPerceive:")
        print("Understanding research question...")

        log_step(
            iteration,
            "Perceive",
            query
        )

        # PLAN
        plan = create_plan(query)

        print("\nPlan:")
        print(plan)

        log_step(
            iteration,
            "Plan",
            plan
        )

        # ACT
        print("\nAct:")

        if plan.startswith("SEARCH:"):

            search_query = plan.replace("SEARCH:", "").strip()

            result = search_web(search_query)

            print("Search result:", result)

            log_step(
                iteration,
                "Act",
                str(result)
            )

            # TOOL FAILURE RECOVERY
            if not result["success"]:

                print("Search failed. Retrying with original question.")

                log_step(
                    iteration,
                    "Recovery",
                    "Search failed"
                )

                query = user_input
                continue

            # Check search results
            if len(result["results"]) == 0:

                print("No search results found.")

                log_step(
                    iteration,
                    "Recovery",
                    "No search results"
                )

                query = search_query + " reliable source"
                continue

            # Fetch top result
            top_result = result["results"][0]

            url = top_result["url"]

            page = fetch_page(url)

            print("\nFetch result:", page)

            log_step(
                iteration,
                "Act",
                str(page)
            )

            # FETCH FAILURE RECOVERY
            if not page["success"]:

                print("Page fetch failed. Refining search.")

                log_step(
                    iteration,
                    "Recovery",
                    "Page fetch failed"
                )

                query = search_query + " reliable source"
                continue

            # OBSERVE
            print("\nObserve:")

            observation = observe_page(
                query,
                page["content"]
            )

            print("Observation:", observation)

            log_step(
                iteration,
                "Observe",
                observation
            )

            # INFORMATION IS SUFFICIENT
            if observation.startswith("SUFFICIENT"):

                print("\nResearch completed successfully.")

                log_step(
                    iteration,
                    "Success",
                    "Information is sufficient"
                )

                return

            # INFORMATION IS NOT SUFFICIENT
            elif observation.startswith("REFINE:"):

                new_query = observation.replace(
                    "REFINE:",
                    ""
                ).strip()

                print("\nRefining search:")
                print(new_query)

                log_step(
                    iteration,
                    "Refine",
                    new_query
                )

                query = new_query
                continue

            # INVALID OBSERVATION
            else:

                print("\nInvalid observation.")

                log_step(
                    iteration,
                    "Recovery",
                    "Invalid observation"
                )

                query = search_query + " reliable information"
                continue

        else:

            print("\nObserve:")
            print("Planner did not return a valid SEARCH action.")

            log_step(
                iteration,
                "Observe",
                "Invalid planner action"
            )

            query = user_input + " reliable information"


    print("\nMaximum iterations reached.")

    log_step(
        MAX_ITERATIONS,
        "Stop",
        "Maximum iteration limit reached"
    )


user_input = input("Enter your research question: ")

run_agent(user_input)
label instantiate_business_policies():
    python:
        uniform_policies_list = []
        organisation_policies_list = []
        unmapped_policies_list = []
        recruitment_policies_list = []
        serum_policies_list = []
        special_policies_list = []

        init_clothing_policies()
        init_organisation_policies()
        init_recruitment_policies()
        init_serum_policies()
        init_special_policies()
    return

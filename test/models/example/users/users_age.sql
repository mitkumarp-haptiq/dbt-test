with users as (
    select 
    name, phone_number, date_of_birth, {{ age_from_dob('date_of_birth') }} as age,
        case
            when {{ age_from_dob('date_of_birth') }} < 18 then 'minor'
            when {{ age_from_dob('date_of_birth') }} >= 18 and {{ age_from_dob('date_of_birth') }} < 60 then 'adult'
            else 'senior'
        end as age_group
    from {{ source('intermediate', 'users') }}
)
select * from users
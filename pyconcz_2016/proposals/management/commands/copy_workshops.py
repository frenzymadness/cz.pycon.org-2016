from django.core.management.base import BaseCommand, CommandError

from pyconcz_2016.proposals.models import Workshop as ProposalWorkshop
from pyconcz_2016.speakers.models import Speaker, Workshop


class Command(BaseCommand):
    def handle(self, *args, **options):
        for proposal in ProposalWorkshop.objects.all().filter(accepted=True):
            workshop, _ = Workshop.objects.get_or_create(
                title=proposal.title,
                defaults=dict(
                    abstract=proposal.abstract,
                    language=proposal.language,
                    difficulty=proposal.difficulty,
                    type=proposal.type,
                    length=proposal.length
                )
            )

            speaker, _ = Speaker.objects.get_or_create(
                email=proposal.email,
                defaults=dict(
                    full_name=proposal.full_name,
                    bio=proposal.bio,
                    twitter=proposal.twitter,
                    github=proposal.github,
                    photo=proposal.photo
                )
            )

            speaker.workshops.add(workshop)

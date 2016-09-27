from django.core.management.base import BaseCommand, CommandError

from pyconcz_2016.proposals.models import Talk as ProposalTalk
from pyconcz_2016.speakers.models import Speaker, Talk


class Command(BaseCommand):
    def handle(self, *args, **options):
        for proposal in ProposalTalk.objects.all().filter(accepted=True):
            talk, _ = Talk.objects.get_or_create(
                title=proposal.title,
                defaults=dict(
                    abstract=proposal.abstract,
                    language=proposal.language,
                    difficulty=proposal.difficulty
                )
            )

            speaker, _ = Speaker.objects.get_or_create(
                email=proposal.email,
                defaults=dict(
                    full_name=proposal.full_name,
                    bio=proposal.bio,
                    twitter=proposal.twitter,
                    github=proposal.github,
                    photo=proposal.photo,
                    talk=talk
                )
            )
